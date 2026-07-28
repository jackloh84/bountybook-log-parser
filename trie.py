"""Trie — insert, search, starts_with. Case-sensitive. Stdlib only."""


class Trie:
    def __init__(self):
        self._root: dict = {}

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True  # end-of-word marker

    def search(self, word: str) -> bool:
        node = self._root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return node.get("$", False)

    def starts_with(self, prefix: str) -> bool:
        node = self._root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True