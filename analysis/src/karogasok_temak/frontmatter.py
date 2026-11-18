"""Adding list keys to YAML front matter without disturbing the rest.

Round-tripping the front matter through a YAML library would reformat every
post in the archive — reordering keys, restyling quotes, rewriting dates — and
bury the one line that actually changed in a diff of hundreds. So this edits the
front matter as text: it finds the block, drops any previous copy of the key,
and appends the new one. Everything it does not recognise it leaves alone.

The parsing is deliberately shallow. It understands exactly the shape this site
writes — ``key:`` followed by ``  - value`` lines, or ``key: [a, b]`` — and
nothing nested. That is enough for ``tema`` and ``kulcsszavak``, and it cannot
silently mangle a structure it does not understand.
"""

from __future__ import annotations

import re
from collections.abc import Sequence

_FRONT_MATTER = re.compile(r"\A(---\n)(.*?\n)(---\n)", re.S)

#: Characters that force a YAML scalar to be quoted.
_NEEDS_QUOTING = set(":#[]{},&*!|>%@`\"'")


def quote(value: str) -> str:
    r"""Render a string as a YAML scalar, quoting only when necessary.

    Args:
        value: The string.

    Returns:
        A YAML-safe scalar.

    Example:
        >>> quote("nyelvtechnológia")
        'nyelvtechnológia'
        >>> quote("gépi tanulás: bevezetés")
        '"gépi tanulás: bevezetés"'
        >>> quote('idézőjel " benne')
        '"idézőjel \\" benne"'
    """
    if value and not (_NEEDS_QUOTING & set(value)) and value.strip() == value:
        return value
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _strip_key(lines: list[str], key: str) -> list[str]:
    """Remove a key and its indented continuation lines."""
    out: list[str] = []
    skipping = False
    for line in lines:
        if skipping:
            if line.startswith((" ", "\t")) or not line.strip():
                continue
            skipping = False
        if line.startswith(f"{key}:"):
            skipping = True
            continue
        out.append(line)
    return out


def set_list_key(front: str, key: str, values: Sequence[str]) -> str:
    r"""Replace ``key`` in a front-matter body with a YAML list.

    Args:
        front: The text between the ``---`` fences, ending in a newline.
        key: The key to set.
        values: The list items. An empty sequence removes the key entirely,
            rather than writing an empty list — a post with no theme should
            have no ``tema`` line at all.

    Returns:
        The updated front-matter body.

    Example:
        >>> print(set_list_key("title: A\n", "tema", ["nyelv", "gép"]), end="")
        title: A
        tema:
          - nyelv
          - gép
        >>> front = "title: A\ntema:\n  - régi\n"
        >>> print(set_list_key(front, "tema", ["új"]), end="")
        title: A
        tema:
          - új
        >>> print(set_list_key(front, "tema", []), end="")
        title: A
    """
    lines = _strip_key(front.splitlines(), key)
    if values:
        lines.append(f"{key}:")
        lines.extend(f"  - {quote(value)}" for value in values)
    return "".join(f"{line}\n" for line in lines)


def _unquote(value: str) -> str:
    """Strip one pair of matching YAML quotes, undoing :func:`quote`."""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def read_list_key(text: str, key: str) -> list[str]:
    r"""Read a list key from a file's front matter, in the shapes this site writes.

    Understands ``key:`` followed by ``  - value`` lines and the flow form
    ``key: [a, "b"]``. The flow form is split on commas, so a value that itself
    contains a comma must use the block form.

    Args:
        text: The complete file contents, front matter first.
        key: The key to read.

    Returns:
        The values, unquoted, in file order. Empty if the key is absent, empty,
        or the file has no front matter — a missing list is not an error here.

    Example:
        >>> src = '---\ntitle: A\nkizart:\n  - vélemény\n  - "x: y"\n---\nSzöveg.\n'
        >>> read_list_key(src, "kizart")
        ['vélemény', 'x: y']
        >>> read_list_key('---\nkizart: [a, "b"]\n---\n', "kizart")
        ['a', 'b']
        >>> read_list_key('---\nkizart: []\n---\n', "kizart")
        []
        >>> read_list_key("Nincs front matter.", "kizart")
        []
    """
    match = _FRONT_MATTER.match(text)
    if match is None:
        return []
    values: list[str] = []
    collecting = False
    for line in match.group(2).splitlines():
        if collecting:
            if line.startswith((" ", "\t")) and line.strip().startswith("- "):
                values.append(_unquote(line.strip()[2:]))
                continue
            break
        if line.startswith(f"{key}:"):
            rest = line[len(key) + 1 :].strip()
            if rest.startswith("[") and rest.endswith("]"):
                inner = rest[1:-1].strip()
                return [_unquote(v) for v in inner.split(",")] if inner else []
            collecting = True
    return values


def update_front_matter(text: str, updates: dict[str, Sequence[str]]) -> str:
    r"""Apply :func:`set_list_key` for several keys to a whole file.

    Args:
        text: The complete file contents, front matter first.
        updates: Key to list of values.

    Returns:
        The updated file contents, body untouched.

    Raises:
        ValueError: If the file does not start with a front-matter block.

    Example:
        >>> src = "---\ntitle: A\n---\n\nSzöveg.\n"
        >>> print(update_front_matter(src, {"tema": ["nyelv"]}), end="")
        ---
        title: A
        tema:
          - nyelv
        ---
        <BLANKLINE>
        Szöveg.
    """
    match = _FRONT_MATTER.match(text)
    if match is None:
        msg = "file does not begin with a YAML front-matter block"
        raise ValueError(msg)
    front = match.group(2)
    for key, values in updates.items():
        front = set_list_key(front, key, values)
    return match.group(1) + front + match.group(3) + text[match.end() :]
