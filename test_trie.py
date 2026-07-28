"""Exact BountyBook test for Trie."""
from trie import Trie

t = Trie()
assert not t.search("anything")
assert not t.starts_with("a")

t.insert("apple")
assert t.search("apple")
assert not t.search("app")
assert not t.search("apples")
assert t.starts_with("app")
assert t.starts_with("apple")
assert t.starts_with("a")
assert not t.starts_with("b")

t.insert("app")
assert t.search("app")
assert t.search("apple")

t.insert("banana"); t.insert("band"); t.insert("bandana")
assert t.search("banana")
assert t.search("band")
assert t.search("bandana")
assert not t.search("ban")
assert t.starts_with("ban")
assert t.starts_with("band")
assert not t.starts_with("xyz")

t.insert("Hello")
assert t.search("Hello")
assert not t.search("hello")
assert not t.starts_with("hel")
assert t.starts_with("Hel")

print("ALL TESTS PASSED")