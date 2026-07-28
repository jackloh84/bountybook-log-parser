"""Verification tests for flatten_dict — exact copy from BountyBook spec."""
from flatten import flatten_dict

# Basic nesting
assert flatten_dict({"a": {"b": 1, "c": 2}}) == {"a.b": 1, "a.c": 2}, "basic nesting"

# Deep nesting
assert flatten_dict({"x": {"y": {"z": 3}}, "n": 0}) == {"x.y.z": 3, "n": 0}, "deep nesting"

# Custom separator
assert flatten_dict({"a": {"b": 1}}, sep="/") == {"a/b": 1}, "custom sep"

# List values are not expanded
assert flatten_dict({"a": {"b": [1, 2, 3]}}) == {"a.b": [1, 2, 3]}, "list value preserved"

# Already flat dict
assert flatten_dict({"x": 1, "y": 2}) == {"x": 1, "y": 2}, "already flat"

# Empty dict
assert flatten_dict({}) == {}, "empty dict"

# Nested empty dict produces no keys
result = flatten_dict({"a": {}})
assert "a" not in result, "empty nested dict adds no keys"

# None values
assert flatten_dict({"a": {"b": None}}) == {"a.b": None}, "None value"

# Mixed depth
r = flatten_dict({"a": {"b": 1}, "c": 2, "d": {"e": {"f": 3}}})
assert r == {"a.b": 1, "c": 2, "d.e.f": 3}, f"mixed: {r}"

print("ALL TESTS PASSED")