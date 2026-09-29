"""The curated theme list: what it may contain, and the checks that keep it sane.

Themes are no longer whatever a clustering happens to find. They are a list the
author owns, in ``analysis/temalista.yaml``; each theme is defined by a handful
of the author's own writings (its *seeds*), and every other writing is placed by how
close it is to them. This module reads that list and refuses a bad one.

The refusals exist because the mistakes are silent otherwise:

* a theme's URL is ``/tema/<urlize(nev)>/`` — Hugo derives it from the name, so
  renaming a theme moves it, and a name Python and Hugo slugify differently
  would put a tag and its hub at different addresses;
* a theme with one or two seeds cannot be told apart from its neighbours —
  measured on this corpus, one seed barely separates members from the rest;
* every name ever published is a URL somebody may hold, so each must still be
  accounted for: as a live theme, a former name that now redirects, or a
  retired theme with a destination.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

#: The three states a theme can be in.
STATES = ("aktiv", "javaslat", "megszunt")

#: Fewest seeds an active theme may have.
MIN_SEEDS = 3

#: A name may use letters (any script), digits, single spaces and hyphens, so
#: that its URL is the same whether Python or Hugo derives it.
_NAME = re.compile(r"^[^\W_](?:[\w -]*[^\W_])?$")


#: How a guest author is credited at the top of a page on this blog:
#: "X vendégposztja", "A guest post by X", "*X írása*".
_GUEST_BYLINE = re.compile(
    r"vendégposztja\b"
    r"|\bguest post by\b"
    r"|^\W*vendégposzt\W"
    r"|^\W*[A-ZÁÉÍÓÖŐÚÜŰ][\w.-]+(?: [A-ZÁÉÍÓÖŐÚÜŰ][\w.-]+)+ írása\b",
    re.IGNORECASE | re.MULTILINE,
)


def has_guest_byline(text: str, *, head: int = 300) -> bool:
    """Whether a page opens with a guest author's byline.

    A seed defines a theme as the author's own subject, so a guest post must
    never be one. Only the opening is read: the author's own posts sometimes
    *mention* guest posts further down (a call for authors, an anniversary).

    Example:
        >>> has_guest_byline("*Tolnai Tímea vendégposztja* A könyv...")
        True
        >>> has_guest_byline("**A guest post by Hannah Little** Introduction")
        True
        >>> has_guest_byline("*Fehér Krisztina írása* Kuhn nagy vitát...")
        True
        >>> has_guest_byline("A Kereső Világ blogon vendégposztoltam a fenti címen")
        False
    """
    return bool(_GUEST_BYLINE.search(text[:head]))


@dataclass(frozen=True)
class Theme:
    """One entry of the theme list.

    Attributes:
        kulcs: Stable internal id. Never reused, never renamed.
        nev: The name readers see; the URL is derived from it.
        leiras: One sentence for the hub and the methods page.
        allapot: ``aktiv``, ``javaslat`` (proposed, not published) or
            ``megszunt`` (retired).
        magok: Seed writings, by page path.
        korabbi_nevek: Former names that now redirect here.
        atiranyitas: For a retired theme, where its URL now leads.
        eredet: Provenance only, e.g. the topic-model cluster it came from.
    """

    kulcs: str
    nev: str
    leiras: str = ""
    allapot: str = "aktiv"
    magok: tuple[str, ...] = ()
    korabbi_nevek: tuple[str, ...] = ()
    atiranyitas: str | None = None
    eredet: Mapping[str, object] = field(default_factory=dict)


def parse(raw: Mapping[str, Any]) -> list[Theme]:
    """Turn the loaded YAML into themes, without judging them.

    Args:
        raw: The parsed file, with a top-level ``temak`` list.

    Returns:
        The themes, in file order.

    Example:
        >>> parse({"temak": [{"kulcs": "a", "nev": "Alfa", "magok": ["x"]}]})[0].magok
        ('x',)
    """
    themes = []
    for entry in raw.get("temak", []) or []:
        themes.append(
            Theme(
                kulcs=str(entry["kulcs"]),
                nev=str(entry["nev"]),
                leiras=str(entry.get("leiras", "")),
                allapot=str(entry.get("allapot", "aktiv")),
                magok=tuple(entry.get("magok", []) or []),
                korabbi_nevek=tuple(entry.get("korabbi_nevek", []) or []),
                atiranyitas=entry.get("atiranyitas"),
                eredet=entry.get("eredet", {}) or {},
            )
        )
    return themes


def load(path: Path) -> list[Theme]:
    """Read and parse ``temalista.yaml``.

    Args:
        path: The file.

    Returns:
        The themes, in file order.
    """
    import yaml

    return parse(yaml.safe_load(path.read_text(encoding="utf-8")))


@dataclass(frozen=True)
class Report:
    """The outcome of validating a theme list.

    Attributes:
        errors: Problems that must be fixed before the list is used.
        warnings: Problems worth a look that do not block.
    """

    errors: tuple[str, ...]
    warnings: tuple[str, ...]

    @property
    def ok(self) -> bool:
        """Whether there are no errors."""
        return not self.errors


def validate(
    themes: Sequence[Theme],
    *,
    pages: Mapping[str, int],
    published_names: Iterable[str] = (),
    min_seeds: int = MIN_SEEDS,
) -> Report:
    """Check a theme list against the corpus and the site's history.

    Args:
        themes: The parsed list.
        pages: Every usable seed — page path mapped to its word count. Future
            and too-short writings must already be left out by the caller.
        published_names: Every theme name the site has ever published.
        min_seeds: Fewest seeds an active theme may have. Defaults to
            :data:`MIN_SEEDS`.

    Returns:
        Errors and warnings.

    Example:
        >>> pages = {"p1": 300, "p2": 300, "p3": 300}
        >>> ok = [Theme("a", "Alfa", magok=("p1", "p2", "p3"))]
        >>> validate(ok, pages=pages).ok
        True
        >>> thin = [Theme("a", "Alfa", magok=("p1",))]
        >>> validate(thin, pages=pages).errors
        ('Alfa: 1 seed(s); an active theme needs at least 3',)
        >>> validate(ok, pages=pages, published_names=["Béta"]).errors[0][:30]
        "published name 'Béta' is not a"
    """
    errors: list[str] = []
    warnings: list[str] = []

    for dup, n in Counter(t.kulcs for t in themes).items():
        if n > 1:
            errors.append(f"kulcs {dup!r} is used {n} times")

    all_names: list[str] = []
    for theme in themes:
        all_names.append(theme.nev)
        all_names.extend(theme.korabbi_nevek)
        if not _NAME.match(theme.nev):
            errors.append(
                f"{theme.nev!r}: use only letters, digits, spaces and hyphens"
            )
        if theme.allapot not in STATES:
            errors.append(f"{theme.nev}: unknown allapot {theme.allapot!r}")
        if theme.allapot == "megszunt":
            if not theme.atiranyitas or not theme.atiranyitas.startswith("/"):
                errors.append(f"{theme.nev}: a retired theme needs an atiranyitas path")
            continue
        missing = [s for s in theme.magok if s not in pages]
        for seed in missing:
            errors.append(f"{theme.nev}: seed {seed} is not a usable page")
        usable = len(theme.magok) - len(missing)
        if theme.allapot == "aktiv" and usable < min_seeds:
            errors.append(
                f"{theme.nev}: {usable} seed(s); an active theme needs at least "
                f"{min_seeds}"
            )

    for name, n in Counter(all_names).items():
        if n > 1:
            errors.append(f"name {name!r} appears {n} times")

    known = set(all_names)
    for name in published_names:
        if name not in known:
            errors.append(
                f"published name {name!r} is not accounted for — keep it, list it "
                f"in korabbi_nevek, or retire it"
            )

    seed_owner = Counter(s for t in themes if t.allapot != "megszunt" for s in t.magok)
    for seed, n in seed_owner.items():
        if n > 1:
            warnings.append(f"seed {seed} belongs to {n} themes")

    return Report(tuple(errors), tuple(warnings))
