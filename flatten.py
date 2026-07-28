"""Flatten nested dicts into single-level dicts with joined keys.

flatten_dict(d: dict, sep: str = '.') -> dict
"""


def flatten_dict(d: dict, sep: str = ".") -> dict:
    """Recursively flatten a nested dict. Non-dict values kept as-is.

    An empty nested dict produces no keys in the output.
    """
    out: dict = {}

    def _walk(node: dict, prefix: str) -> None:
        for key, value in node.items():
            new_key = f"{prefix}{sep}{key}" if prefix else key
            if isinstance(value, dict):
                if value:  # non-empty nested dict — descend
                    _walk(value, new_key)
                # empty nested dict → produce no keys
            else:
                out[new_key] = value

    _walk(d, "")
    return out