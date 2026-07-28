"""BloomFilter — probabilistic membership test using bit array + k hash functions.

Uses standard formulas:
  m = -(n * ln(p)) / (ln(2)^2)
  k = (m/n) * ln(2)
  h_i(x) = (hash1(x) + i * hash2(x)) % m
"""
import math
import hashlib


class BloomFilter:
    def __init__(self, capacity: int, fp_rate: float):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        if not (0 < fp_rate < 1):
            raise ValueError("fp_rate must be in (0, 1)")
        n = capacity
        p = fp_rate
        ln2 = math.log(2)
        m = math.ceil(-(n * math.log(p)) / (ln2 * ln2))
        k = max(1, round((m / n) * ln2))
        self._capacity = n
        self._fp_rate = p
        self._m = m
        self._k = k
        # bit array stored as bytearray of size ceil(m/8)
        self._bytes = bytearray((m + 7) // 8)

    @property
    def bit_array_size(self) -> int:
        return self._m

    @property
    def num_hash_functions(self) -> int:
        return self._k

    def _hashes(self, item: str) -> tuple[int, int]:
        """Return (h1, h2) — two 64-bit independent hashes."""
        b = item.encode("utf-8")
        h1_bytes = hashlib.md5(b).digest()[:8]
        h2_bytes = hashlib.sha256(b).digest()[:8]
        h1 = int.from_bytes(h1_bytes, "big")
        h2 = int.from_bytes(h2_bytes, "big")
        return h1, h2

    def _set_bit(self, idx: int) -> None:
        byte_idx = idx // 8
        bit_idx = idx % 8
        self._bytes[byte_idx] |= (1 << bit_idx)

    def _get_bit(self, idx: int) -> bool:
        byte_idx = idx // 8
        bit_idx = idx % 8
        return bool(self._bytes[byte_idx] & (1 << bit_idx))

    def add(self, item: str) -> None:
        h1, h2 = self._hashes(item)
        m = self._m
        for i in range(self._k):
            self._set_bit((h1 + i * h2) % m)

    def contains(self, item: str) -> bool:
        h1, h2 = self._hashes(item)
        m = self._m
        for i in range(self._k):
            if not self._get_bit((h1 + i * h2) % m):
                return False
        return True


if __name__ == "__main__":
    bf = BloomFilter(capacity=1000, fp_rate=0.01)

    words = ["apple", "banana", "cherry", "date", "elderberry"]
    for w in words:
        bf.add(w)
    for w in words:
        assert bf.contains(w), f"False negative: {w}"

    assert bf.bit_array_size > 0
    assert bf.num_hash_functions >= 2
    print("All tests passed")