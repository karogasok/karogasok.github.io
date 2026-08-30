#!/usr/bin/env python3
"""Shared machinery for the two archive importers.

Both the Blogspot and the WordPress import turn a decade-old blob of
hand-written HTML into a Markdown file with front matter, and both have to deal
with the same three problems: converting the markup, deciding what to do about
media that may or may not still exist, and writing down what was dropped.

The governing rule for all of it is that the archive is not curated. Nothing
here rewrites a sentence, fixes a typo, drops a post for being weak, or
modernises a link. The only things it is allowed to change are mechanical: the
markup format, and the location of an image that has been copied locally so it
survives the host it came from.

Stdlib only, on purpose. These are one-shot scripts kept in the repo so the
import can be re-run years from now, and a re-run should not begin with
resurrecting a dependency set.
"""

from __future__ import annotations

import csv
import hashlib
import html
import re
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "static" / "archivum" / "img"
OUT_DIR = ROOT / "scripts" / "out"
CONTENT_DIR = ROOT / "content" / "archivum"

USER_AGENT = "karogasok-archive-importer/1.0 (+https://karogasok.github.io/)"

# Hosts whose images are worth copying locally: they are the ones the post
# actually owns, and the ones that vanish when the account does.
SELF_HOSTED = (
    "bp.blogspot.com",
    "blogger.googleusercontent.com",
    "ggpht.com",
    "googleusercontent.com",
    "blog.crowintelligence.org",
    "crowintelligence.org",
    "files.wordpress.com",
)

# Jetpack's image CDN. It fronts the blog's own uploads under a wp.com hostname,
# with the real origin as the first path segment and a resize in the query. Left
# alone these look like somebody else's images and are not copied, so they are
# unwrapped back to the origin first — which also gets the full-size original
# rather than whatever crop the theme happened to ask for.
PHOTON = re.compile(r"^https?://i[0-9]\.wp\.com/(?P<rest>[^?]+)")

# Zemanta was a "related content" widget that shut down years ago. Every one of
# its images is a guaranteed 404, so they are removed rather than copied as
# broken markup. Each removal is logged.
DEAD_HOSTS = ("img.zemanta.com", "www.zemanta.com", "i.zemanta.com")

EMBED_HOSTS = {
    "youtube.com": "YouTube",
    "youtu.be": "YouTube",
    "youtube-nocookie.com": "YouTube",
    "player.vimeo.com": "Vimeo",
    "vimeo.com": "Vimeo",
    "gist.github.com": "GitHub Gist",
    "slideshare.net": "SlideShare",
    "scribd.com": "Scribd",
    "docs.google.com": "Google Docs",
}

HU_MAP = str.maketrans({
    "á": "a", "é": "e", "í": "i", "ó": "o", "ö": "o", "ő": "o",
    "ú": "u", "ü": "u", "ű": "u",
    "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ö": "O", "Ő": "O",
    "Ú": "U", "Ü": "U", "Ű": "U",
})


def slugify(text: str, maxlen: int = 70) -> str:
    """ASCII slug from Hungarian text.

    ``ő`` and ``ű`` decompose to ``o`` and ``u`` rather than being dropped, which
    is what NFKD alone would do to them after stripping the combining accent.
    """
    text = text.translate(HU_MAP)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    if len(text) > maxlen:
        text = text[:maxlen].rsplit("-", 1)[0]
    return text or "bejegyzes"


def yaml_quote(value: str) -> str:
    """Quote a scalar for YAML front matter."""
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


@dataclass
class Report:
    """What the import did, and what it could not do.

    Two files come out of every run: a manifest of every post considered
    (including the ones skipped, and why), and a TODO list of media that could
    not be retrieved. Neither is optional — an import that silently drops a
    hundred images looks exactly like one that worked.
    """

    name: str
    rows: list[dict] = field(default_factory=list)
    todos: list[str] = field(default_factory=list)
    counts: dict[str, int] = field(default_factory=dict)

    def count(self, key: str, n: int = 1) -> None:
        self.counts[key] = self.counts.get(key, 0) + n

    def todo(self, message: str) -> None:
        self.todos.append(message)

    def write(self) -> None:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        if self.rows:
            fields = list(self.rows[0].keys())
            path = OUT_DIR / f"{self.name}-manifest.csv"
            with path.open("w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=fields)
                w.writeheader()
                w.writerows(self.rows)
            print(f"  manifest: {path.relative_to(ROOT)}  ({len(self.rows)} rows)")

        path = OUT_DIR / f"{self.name}-TODO.txt"
        header = [
            f"# {self.name}: media that could not be imported",
            "#",
            "# Each line is something the importer could not retrieve or chose not to",
            "# keep. Nothing here blocks the site; it is the record of what the archive",
            "# lost between publication and import.",
            "",
        ]
        path.write_text("\n".join(header + (self.todos or ["(nothing)"])) + "\n", encoding="utf-8")
        print(f"  todo:     {path.relative_to(ROOT)}  ({len(self.todos)} entries)")

    def summary(self) -> str:
        return "\n".join(f"  {k:.<40} {v}" for k, v in sorted(self.counts.items()))


class MediaResolver:
    """Decides what happens to a URL found in imported markup.

    Four outcomes, returned as ``(status, value)``:

    ``local``  the file was copied into ``static/archivum/img/`` and the value is
               the local path. Used for hosts tied to the original account, which
               are the ones that disappear when the account does.
    ``keep``   leave the URL exactly as written. A link to someone else's site is
               still that link, and rewriting it would misrepresent where the
               post pointed.
    ``dead``   the host is known to be gone (Zemanta), so the element is removed.
    ``lost``   the server answered 404. The image is gone for good, and the
               importer says so rather than leaving markup that renders as a
               broken-image icon.

    The ``lost`` case is the interesting one. Google emptied the Blogger picture
    albums: the Takeout contains no image files, the albums report zero items,
    and the live blog 404s the same URLs. Roughly two hundred images from
    2010-2013 no longer exist anywhere. Rendering a broken <img> for each would
    be silent data loss dressed up as content; dropping them without trace would
    be worse. So each becomes a visible note naming the file that used to be
    there and linking the URL it lived at.

    A transient network failure is *not* treated as ``lost`` — that URL is kept
    as an image, because it may well come back.
    """

    def __init__(self, report: Report, download: bool = True) -> None:
        self.report = report
        self.download = download
        self.cache: dict[str, tuple[str, str | None]] = {}
        IMG_DIR.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _host(url: str) -> str:
        m = re.match(r"(?:https?:)?//([^/]+)", url)
        return (m.group(1) if m else "").lower()

    @staticmethod
    def _encode(url: str) -> str:
        """Percent-encode the non-ASCII parts of a URL.

        WordPress happily stores an upload called ``DALL·E-2023-...png`` and
        writes the raw character straight into the src. urllib refuses to send a
        non-ASCII request line, so the fetch fails with a UnicodeEncodeError that
        reads like the file is missing when it is merely spelled in Unicode.
        ``%`` stays safe so an already-encoded URL is not encoded twice.
        """
        parts = urllib.parse.urlsplit(url)
        return urllib.parse.urlunsplit((
            parts.scheme,
            parts.netloc.encode("idna").decode("ascii") if any(ord(c) > 127 for c in parts.netloc) else parts.netloc,
            urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;=~"),
            urllib.parse.quote(parts.query, safe="/%:@!$&'()*+,;=?~"),
            parts.fragment,
        ))

    @staticmethod
    def _unproxy(url: str) -> str:
        m = PHOTON.match(url)
        return f"https://{m.group('rest')}" if m else url

    def _self_hosted(self, url: str) -> bool:
        return any(h in self._host(url) for h in SELF_HOSTED)

    def resolve(self, url: str, context: str, kind: str = "img") -> tuple[str, str | None]:
        """Resolve one URL. *kind* is ``img`` or ``link``."""
        if not url or url.startswith(("data:", "#", "mailto:", "javascript:")):
            return ("keep", url)
        if url.startswith("//"):
            url = "https:" + url
        url = self._unproxy(url)

        if any(h in self._host(url) for h in DEAD_HOSTS):
            self.report.count(f"{kind}: removed, host shut down")
            self.report.todo(f"DROPPED (dead host)  {context}  {url}")
            return ("dead", None)

        if not self._self_hosted(url):
            self.report.count(f"{kind}: left on its original host")
            return ("keep", url)

        if url in self.cache:
            status, value = self.cache[url]
            self.report.count(f"{kind}: {status} (already known)")
            return (status, value)

        if not self.download:
            return ("keep", url)

        ext = re.search(r"\.(jpe?g|png|gif|webp|svg|bmp)(?:$|\?)", url, re.I)
        suffix = ("." + ext.group(1).lower()) if ext else ".jpg"
        name = hashlib.sha1(url.encode()).hexdigest()[:16] + suffix
        dest = IMG_DIR / name

        if dest.exists():
            out = ("local", f"/archivum/img/{name}")
            self.cache[url] = out
            self.report.count(f"{kind}: already downloaded")
            return out

        try:
            req = urllib.request.Request(self._encode(url), headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                payload = resp.read()
            if not payload:
                raise ValueError("empty response")
            dest.write_bytes(payload)
            out = ("local", f"/archivum/img/{name}")
            self.report.count(f"{kind}: downloaded")
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 410):
                # Gone, confirmed by the server. Say so.
                out = ("lost", url)
                self.report.count(f"{kind}: gone (404)")
                self.report.todo(f"GONE {exc.code}  {context}  {url}")
            else:
                out = ("keep", url)
                self.report.count(f"{kind}: fetch failed ({exc.code}), URL kept")
                self.report.todo(f"FAILED {exc}  {context}  {url}")
        except (urllib.error.URLError, ValueError, OSError, TimeoutError) as exc:
            # Could be the network rather than the file. Keep the URL.
            out = ("keep", url)
            self.report.count(f"{kind}: fetch failed, URL kept")
            self.report.todo(f"FAILED {exc}  {context}  {url}")

        self.cache[url] = out
        return out

    def link(self, url: str, context: str) -> str:
        """Resolve an <a href>. A link is never 'lost' — it stays a link."""
        status, value = self.resolve(url, context, kind="link")
        if status == "local":
            return value
        return url


class HTMLToMarkdown(HTMLParser):
    """Convert a decade of Blogger and WordPress HTML into Markdown.

    Deliberately conservative. Structures with an unambiguous Markdown
    equivalent — paragraphs, headings, lists, emphasis, links, images, quotes,
    code — are converted. Anything else is passed through as raw HTML, which
    Goldmark renders because the site sets ``markup.goldmark.renderer.unsafe``.
    That combination is the point: the conversion never has to guess, and a
    construct it does not understand survives instead of being flattened.

    Embeds are the one exception. A YouTube or Vimeo iframe and a Gist
    ``<script>`` cannot be passed through on a site that ships no JavaScript and
    frames nothing, so each becomes a plain labelled link to the thing it was
    embedding. The reader can still get there; nothing is silently lost.
    """

    INLINE_WRAP = {"strong": "**", "b": "**", "em": "*", "i": "*", "code": "`"}
    BLOCK = {
        "p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li",
        "blockquote", "pre", "table", "tr", "section", "article", "figure",
        "figcaption", "hr", "center",
    }
    DROP = {"script", "style", "noscript", "meta", "link", "form", "button"}
    PASSTHROUGH = {"table", "thead", "tbody", "tr", "td", "th", "sup", "sub", "abbr"}

    def __init__(self, media: MediaResolver, context: str) -> None:
        super().__init__(convert_charrefs=True)
        self.media = media
        self.context = context
        self.blocks: list[str] = []
        self.buf: list[str] = []
        self.list_stack: list[str] = []
        self.quote_depth = 0
        self.in_pre = False
        self.skip_depth = 0
        self.pending_link: list[str] | None = None
        self.raw_depth = 0
        # Emphasis that is still open when a block ends. Blogger's editor
        # routinely wrote <b> around a whole post and put <div>s inside it, so a
        # bold run genuinely spans paragraphs. Markdown has no such thing: an
        # unpaired ** is printed literally. Each block therefore closes what is
        # open and the next one reopens it.
        self.open_inline: list[str] = []
        # <pre> is buffered whole and emitted on the closing tag. Emitting the
        # opening fence into the normal stream meant any block tag inside the
        # <pre> — and Blogger put <div>s and <br>s inside them freely — flushed
        # a block between the fence and its closer. The fence never closed, and
        # every remaining paragraph in the post rendered as literal text.
        self.pre_buf: list[str] = []
        # Where each open wrapper's marker sits in the buffer, so the text it
        # actually covers can be inspected when it closes.
        self.inline_at: list[int] = []

    # -- helpers -------------------------------------------------------

    def _flush(self, prefix: str = "") -> None:
        text = "".join(self.buf) + "".join(reversed(self.open_inline))
        # Reopen whatever is still open at the top of the next block.
        self.buf = list(self.open_inline)
        text = text.strip()
        # A wrapper that ended up around nothing is noise, not emphasis.
        while True:
            stripped = re.sub(r"^(\*\*|\*|`)\s*\1$", "", text).strip()
            if stripped == text:
                break
            text = stripped
        if not text or not re.sub(r"[*`\s]", "", text):
            return
        if self.quote_depth:
            text = "\n".join("> " + ln for ln in text.split("\n"))
        self.blocks.append(prefix + text if prefix else text)

    def _emit(self, text: str) -> None:
        self.buf.append(text)

    # -- parser hooks --------------------------------------------------

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)

        if self.in_pre:
            # Inside a code block only a line break means anything; a <code> or
            # <span> in there is presentation, and its markers would end up in
            # the code itself.
            if tag == "br":
                self.pre_buf.append("\n")
            return

        if self.raw_depth:
            self._emit(self.get_starttag_text() or "")
            if tag in self.PASSTHROUGH:
                self.raw_depth += 1
            return

        if tag in self.DROP:
            # A Gist is delivered as a <script src=...>. There is no script on
            # this site, so it becomes a link to the Gist itself.
            src = a.get("src", "")
            if tag == "script" and "gist.github.com" in src:
                url = src.rsplit(".js", 1)[0]
                self._flush()
                self.blocks.append(f"[GitHub Gist]({url})")
                self.media.report.count("gist embeds turned into links")
            self.skip_depth += 1
            return
        if self.skip_depth:
            return

        if tag in ("iframe", "embed", "object"):
            src = a.get("src") or a.get("data") or ""
            label = next((v for k, v in EMBED_HOSTS.items() if k in src), "Beágyazott tartalom")
            if src:
                self._flush()
                self.blocks.append(f"[{label}]({src})")
                self.media.report.count(f"{label} embeds turned into links")
            return

        if tag == "br":
            # Two trailing spaces: a Markdown hard break. Blogger authors used
            # <br> for real line breaks, and a soft newline would collapse them.
            self._emit("  \n")
            return

        if tag == "hr":
            self._flush()
            self.blocks.append("---")
            return

        if tag == "img":
            status, src = self.media.resolve(a.get("src", ""), self.context, kind="img")
            alt = (a.get("alt") or "").replace("]", "\\]")
            if status == "dead":
                return
            if status == "lost":
                # Raw HTML, which Goldmark passes through. A broken <img> would
                # say nothing; this says what was here and where it lived.
                name = src.rstrip("/").rsplit("/", 1)[-1] or src
                label = alt or name
                self._emit(
                    f'<span class="lost-media">Hiányzó kép: '
                    f'<a href="{src}" rel="nofollow noopener">{label}</a></span>'
                )
                return
            self._emit(f"![{alt}]({src})")
            return

        if tag == "a":
            href = a.get("href", "")
            if href and not href.startswith(("#", "javascript:")):
                href = self.media.link(href, self.context)
            self.pending_link = [href]
            self._emit("[")
            return

        if tag in self.INLINE_WRAP:
            token = self.INLINE_WRAP[tag]
            self.open_inline.append(token)
            self.inline_at.append(len(self.buf))
            self._emit(token)
            return

        if tag == "pre":
            self._flush()
            self.in_pre = True
            self.pre_buf = []
            return

        if tag == "blockquote":
            self._flush()
            self.quote_depth += 1
            return

        if tag in ("ul", "ol"):
            self._flush()
            self.list_stack.append(tag)
            return

        if tag == "li":
            self._flush()
            depth = max(0, len(self.list_stack) - 1)
            marker = "1. " if (self.list_stack and self.list_stack[-1] == "ol") else "- "
            self._emit("  " * depth + marker)
            return

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._flush()
            # Demoted one level: the post title is the page's h1, so an h1 inside
            # the body would be a second one.
            level = min(6, int(tag[1]) + 1)
            self._emit("#" * level + " ")
            return

        if tag in self.PASSTHROUGH:
            self._flush()
            self.raw_depth = 1
            self._emit(self.get_starttag_text() or "")
            return

        if tag in self.BLOCK:
            self._flush()
            return

    def handle_endtag(self, tag):
        if self.in_pre and tag != "pre":
            return

        if self.raw_depth:
            self._emit(f"</{tag}>")
            if tag in self.PASSTHROUGH:
                self.raw_depth -= 1
                if self.raw_depth == 0:
                    self._flush()
            return

        if tag in self.DROP:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return

        if tag == "a" and self.pending_link is not None:
            href = self.pending_link[0]
            self.pending_link = None
            self._emit(f"]({href})")
            return

        if tag in self.INLINE_WRAP:
            token = self.INLINE_WRAP[tag]
            if token not in self.open_inline:
                return
            # Remove the innermost matching opener, not every one of them:
            # nested <b><b> is rare but real in pasted markup.
            for i in range(len(self.open_inline) - 1, -1, -1):
                if self.open_inline[i] == token:
                    del self.open_inline[i]
                    idx = self.inline_at.pop(i) if i < len(self.inline_at) else None
                    break
            else:
                idx = None

            if idx is None or idx >= len(self.buf):
                self._emit(token)
                return

            content = "".join(self.buf[idx + 1:])

            # CommonMark will not open emphasis on whitespace, so <b> around a
            # bare separator — and Blogger produced <b> - </b> constantly — comes
            # out as a literal "** - **". It is not emphasis; drop the markers.
            if not content.strip(" \t\n\r-–—·•:;,.|/"):
                self.buf[idx] = ""
                return

            # Likewise "** text **" fails the flanking rules. Same emphasis,
            # same words: move the padding outside the markers.
            lead = content[: len(content) - len(content.lstrip())]
            trail = content[len(content.rstrip()) :]
            if lead or trail:
                self.buf[idx] = lead + token
                del self.buf[idx + 1:]
                self._emit(content.strip())
            self._emit(token + trail)
            return

        if tag == "pre":
            code = "".join(self.pre_buf).strip("\n")
            self.pre_buf = []
            self.in_pre = False
            if code.strip():
                # A fence longer than any run of backticks inside the code, so
                # a pasted snippet containing ``` cannot close it early.
                longest = max((len(m) for m in re.findall(r"`+", code)), default=0)
                fence = "`" * max(3, longest + 1)
                self.blocks.append(f"{fence}\n{code}\n{fence}")
            return

        if tag == "blockquote":
            self._flush()
            self.quote_depth = max(0, self.quote_depth - 1)
            return

        if tag in ("ul", "ol"):
            self._flush()
            if self.list_stack:
                self.list_stack.pop()
            return

        if tag in ("li", "p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "figcaption", "center"):
            self._flush()
            return

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.in_pre:
            self.pre_buf.append(data)
            return
        if self.raw_depth:
            self._emit(data)
            return
        # Collapse the whitespace that Blogger's editor left everywhere, but do
        # not touch a hard break that has already been emitted.
        text = re.sub(r"[ \t\r\f\v]*\n[ \t\r\f\v]*", " ", data)
        text = re.sub(r"  +", " ", text)
        if text.strip() or (self.buf and not self.buf[-1].endswith(("\n", " "))):
            self._emit(text)

    def close(self):
        super().close()
        self._flush()

    def markdown(self) -> str:
        out: list[str] = []
        for block in self.blocks:
            block = block.strip()
            if block:
                out.append(block)
        text = "\n\n".join(out)
        text = re.sub(r"\n{3,}", "\n\n", text)

        # A last pass over the bold markers only. Single asterisks are left
        # alone on purpose: this is a linguistics blog, and a leading * marks an
        # ungrammatical form ("*Ez mondat lenni helytelen"). Rewriting those
        # would corrupt the argument the post is making.
        #
        # Two patterns survive the tag-level handling, both from markup that
        # closes and reopens across a block boundary:
        #   ****        one bold run ending where the next begins
        #   ** text **  padding inside the markers, which CommonMark will not
        #               open emphasis on, so it prints the asterisks instead
        text = re.sub(r"\*\*([ \t]*)\*\*", r"\1", text)
        text = re.sub(
            r"\*\*([ \t]*)([^\n*][^\n]*?)([ \t]*)\*\*",
            lambda m: (f"{m.group(1)}**{m.group(2).strip()}**{m.group(3)}"
                       if m.group(2).strip() else m.group(1) + m.group(3)),
            text,
        )
        text = re.sub(r"[ \t]+\n", lambda m: "  \n" if m.group(0).startswith("  ") else "\n", text)
        return text.strip() + "\n"


def to_markdown(raw_html: str, media: MediaResolver, context: str) -> str:
    parser = HTMLToMarkdown(media, context)
    parser.feed(raw_html)
    parser.close()
    return parser.markdown()


def validate_markdown(body: str, context: str, report: Report) -> None:
    """Flag conversions that will render as something other than prose.

    An unclosed code fence is the dangerous one: it does not fail, it silently
    swallows the rest of the post and renders every remaining paragraph as
    literal text, asterisks and all. It cost 98 pages before it was noticed, so
    it is now checked on every conversion rather than found by reading.
    """
    if body.count("```") % 2:
        report.count("BROKEN: unclosed code fence")
        report.todo(f"MARKDOWN unclosed code fence  {context}")
    # An odd number of ** in a paragraph prints them literally.
    for para in body.split("\n\n"):
        if para.count("**") % 2 and "***" not in para:
            report.count("BROKEN: unpaired bold marker")
            report.todo(f"MARKDOWN unpaired ** in a paragraph  {context}")
            break


def write_post(path: Path, front: dict, body: str) -> None:
    """Write one archive post: YAML front matter, then the converted body."""
    lines = ["---"]
    for key, value in front.items():
        if value is None or value == [] or value == "":
            continue
        if isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {yaml_quote(v)}" for v in value)
        elif isinstance(value, str) and key in ("date", "publishDate", "lastmod"):
            lines.append(f"{key}: {value}")
        else:
            lines.append(f"{key}: {yaml_quote(value)}")
    lines.append("---")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n\n" + body, encoding="utf-8")
