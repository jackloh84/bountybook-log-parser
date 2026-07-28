"""Verification tests from BountyBook spec for log_parser."""
from log_parser import parse_log

LOG = """127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
192.168.1.5 - - [10/Oct/2000:13:57:00 -0700] "POST /api/data HTTP/1.1" 404 512
10.0.0.1 - alice [11/Oct/2000:09:00:00 +0000] "DELETE /resource/42 HTTP/2.0" 204 0
bad line that should be skipped"""

rows = parse_log(LOG)
assert len(rows) == 3, f"expected 3 parsed rows, got {len(rows)}"

r0 = rows[0]
assert r0["ip"] == "127.0.0.1", f"ip: {r0['ip']}"
assert r0["user"] == "frank", f"user: {r0['user']}"
assert r0["method"] == "GET", f"method: {r0['method']}"
assert r0["path"] == "/apache_pb.gif", f"path: {r0['path']}"
assert r0["protocol"] == "HTTP/1.0", f"protocol: {r0['protocol']}"
assert r0["status"] == 200, f"status: {r0['status']}"
assert r0["bytes"] == 2326, f"bytes: {r0['bytes']}"
assert "10/Oct/2000:13:55:36 -0700" in r0["timestamp"], f"timestamp: {r0['timestamp']}"

r1 = rows[1]
assert r1["user"] is None, f"dash user should be None, got: {r1['user']}"
assert r1["status"] == 404
assert r1["method"] == "POST"

r2 = rows[2]
assert r2["user"] == "alice"
assert r2["method"] == "DELETE"
assert r2["status"] == 204
assert r2["bytes"] == 0

# bytes=- edge case
LOG2 = '1.2.3.4 - - [01/Jan/2024:00:00:00 +0000] "HEAD / HTTP/1.1" 304 -'
rows2 = parse_log(LOG2)
assert rows2[0]["bytes"] == 0, f"bytes from '-' should be 0, got {rows2[0]['bytes']}"

print("ALL TESTS PASSED")