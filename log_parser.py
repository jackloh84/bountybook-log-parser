"""Apache Combined Log Format parser.

parse_log(log_text: str) -> list[dict]

Returns one dict per valid log line with keys:
  ip, user, timestamp, method, path, protocol, status (int), bytes (int)
"""
import re

# Apache Combined Log Format regex
# Example:
# 127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
_LOG_RE = re.compile(
    r'^(?P<ip>\S+)\s+'                # client IP
    r'\S+\s+'                         # identd (always '-' or value)
    r'(?P<user>\S+)\s+'               # userid (could be '-')
    r'\[(?P<timestamp>[^\]]+)\]\s+'   # timestamp in brackets
    r'"(?P<method>\S+)\s+'            # request method
    r'(?P<path>\S+)\s+'               # request path
    r'(?P<protocol>[^"]+)"\s+'        # protocol
    r'(?P<status>\d+)\s+'             # status code
    r'(?P<bytes>\d+|-)\s*$'           # bytes (or '-')
)

_METHOD_ALLOWED = {"GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH", "TRACE", "CONNECT"}


def parse_log(log_text: str) -> list[dict]:
    """Parse Apache Combined Log Format text into a list of dicts.

    Lines that don't match the format are silently skipped.
    """
    rows: list[dict] = []
    for raw_line in log_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        m = _LOG_RE.match(line)
        if not m:
            continue
        d = m.groupdict()

        # user: '-' -> None
        user = None if d["user"] == "-" else d["user"]

        # bytes: '-' -> 0
        bytes_raw = d["bytes"]
        bytes_val = 0 if bytes_raw == "-" else int(bytes_raw)

        rows.append({
            "ip": d["ip"],
            "user": user,
            "timestamp": d["timestamp"],
            "method": d["method"],
            "path": d["path"],
            "protocol": d["protocol"],
            "status": int(d["status"]),
            "bytes": bytes_val,
        })
    return rows