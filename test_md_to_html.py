"""Exact BountyBook verification test for md_to_html."""
from md_to_html import convert

assert convert("# Hello") == "<h1>Hello</h1>", f"h1: got {convert('# Hello')}"
assert convert("## World") == "<h2>World</h2>", f"h2: got {convert('## World')}"
assert convert("### Deep") == "<h3>Deep</h3>", f"h3: got {convert('### Deep')}"
assert convert("Hello world") == "<p>Hello world</p>", f"p: got {convert('Hello world')}"
assert convert("**bold**") == "<p><strong>bold</strong></p>", f"bold: {convert('**bold**')}"
assert convert("*italic*") == "<p><em>italic</em></p>", f"italic: {convert('*italic*')}"
assert convert("`code`") == "<p><code>code</code></p>", f"code: {convert('`code`')}"

result = convert("# Title\n\nSome **bold** text.")
assert "<h1>Title</h1>" in result, f"h1 missing: {result}"
assert "<strong>bold</strong>" in result, f"strong missing: {result}"
assert "<p>" in result, f"p missing: {result}"

heading_inline = convert("## Hello **world**")
assert heading_inline == "<h2>Hello <strong>world</strong></h2>", f"heading inline: {heading_inline}"

# empty string
assert convert("") == ""

print("ALL TESTS PASSED")