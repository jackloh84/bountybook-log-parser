"""Exact BountyBook verification for cicd_comparison.json."""
import json, re
from pathlib import Path

data = json.loads(Path("/home/ubuntu/projects/bountybook/cicd_comparison.json").read_text())

assert "generated_at" in data
assert re.match(r"\d{4}-\d{2}-\d{2}", data["generated_at"])
assert "platforms" in data
assert len(data["platforms"]) == 5, f"expected 5, got {len(data['platforms'])}"

expected = {"GitHub Actions", "GitLab CI/CD", "CircleCI", "Jenkins", "Drone CI"}
found = {p["name"] for p in data["platforms"]}
assert found == expected, f"name mismatch: {found ^ expected}"

required = [
    "name", "open_source", "self_hosted_runner", "free_tier_minutes", "free_tier_notes",
    "config_format", "config_file", "parallel_jobs", "matrix_builds", "docker_support",
    "secret_management", "best_for", "limitations", "pricing_summary"
]
for p in data["platforms"]:
    for f in required:
        assert f in p, f"missing field '{f}' in {p.get('name','?')}"
    assert isinstance(p["open_source"], bool)
    assert isinstance(p["self_hosted_runner"], bool)
    assert isinstance(p["parallel_jobs"], bool)
    assert isinstance(p["matrix_builds"], bool)
    assert isinstance(p["docker_support"], bool)
    assert isinstance(p["free_tier_minutes"], int)
    assert len(p["best_for"]) > 10
    assert len(p["limitations"]) > 10
    assert isinstance(p["config_format"], str) and len(p["config_format"]) > 0

print("ALL TESTS PASSED")