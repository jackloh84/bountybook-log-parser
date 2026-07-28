"""Tiny Markdown -> HTML converter (h1-h3, bold, italic, code, paragraphs)."""
import re


_HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)$")


def _apply_inline(text: str) -> str:
    """Apply **bold**, *italic*, `code` in that order (bold before italic)."""
    # Code first to protect its content from bold/italic
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # Bold before italic — important because * is a subset of **
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def convert(markdown: str) -> str:
    if not markdown:
        return ""

    out: list[str] = []
    para: list[str] = []

    def flush_para() -> None:
        if para:
            content = " ".join(para)
            out.append(f"<p>{_apply_inline(content)}</p>")
            para.clear()

    for raw_line in markdown.split("\n"):
        line = raw_line.rstrip()
        if not line.strip():
            flush_para()
            continue
        m = _HEADING_RE.match(line)
        if m:
            flush_para()
            level = len(m.group(1))
            content = m.group(2).strip()
            out.append(f"<h{level}>{_apply_inline(content)}</h{level}>")
        else:
            para.append(line.strip())

    flush_para()
    return "".join(out)