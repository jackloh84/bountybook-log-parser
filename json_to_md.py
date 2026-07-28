"""Convert a list of dicts to a GitHub-Flavored Markdown table."""
from typing import Iterable


def json_to_markdown_table(data: list[dict]) -> str:
    """Render list[dict] to GFM Markdown table string.

    - Column order: keys from the first dict
    - Cell values: str(value)
    - Single-space padding around cells
    - Each row ends with newline
    """
    if not data:
        return ""

    cols = list(data[0].keys())
    # Compute widths per column from header + all values
    widths = {c: len(c) for c in cols}
    for row in data:
        for c in cols:
            widths[c] = max(widths[c], len(str(row.get(c, ""))))

    lines: list[str] = []
    # Header
    lines.append("| " + " | ".join(c.ljust(widths[c]) for c in cols) + " |")
    # Separator
    lines.append("| " + " | ".join("-" * widths[c] for c in cols) + " |")
    # Data rows
    for row in data:
        lines.append("| " + " | ".join(str(row.get(c, "")).ljust(widths[c]) for c in cols) + " |")

    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sample = [
        {"name": "Alice", "age": 30, "city": "Paris"},
        {"name": "Bob",   "age": 25, "city": "Berlin"},
    ]
    print(json_to_markdown_table(sample), end="")