"""Convert list[dict] to aligned Markdown table."""
from typing import Iterable


def render_table(rows: list[dict], columns: list[str] | None = None) -> str:
    if not rows:
        return ""

    if columns is None:
        columns = list(rows[0].keys())
    else:
        columns = list(columns)

    # Values per row as strings, None -> ""
    def _val(row, c):
        v = row.get(c)
        return "" if v is None else str(v)

    # Compute column widths
    widths = {c: len(c) for c in columns}
    for row in rows:
        for c in columns:
            widths[c] = max(widths[c], len(_val(row, c)))

    lines: list[str] = []
    # Header
    lines.append("| " + " | ".join(c.ljust(widths[c]) for c in columns) + " |")
    # Separator
    lines.append("| " + " | ".join("-" * widths[c] for c in columns) + " |")
    # Data rows
    for row in rows:
        lines.append("| " + " | ".join(_val(row, c).ljust(widths[c]) for c in columns) + " |")

    return "\n".join(lines)


if __name__ == "__main__":
    sample = [
        {"name": "Alice", "age": 30, "city": "NYC"},
        {"name": "Bob",   "age": 25, "city": "LA"},
        {"name": "Carol", "age": 35, "city": "Chicago"},
    ]
    print(render_table(sample))