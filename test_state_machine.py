"""Exact BountyBook test for StateMachine."""
from state_machine import StateMachine

sm = StateMachine("idle")
sm.add_transition("idle", "start", "running")
sm.add_transition("running", "pause", "paused")
sm.add_transition("paused", "resume", "running")
sm.add_transition("running", "stop", "idle")

assert sm.state == "idle"
assert sm.trigger("start") == True
assert sm.state == "running"
assert sm.trigger("pause") == True
assert sm.state == "paused"
assert sm.trigger("resume") == True
assert sm.state == "running"
assert sm.trigger("stop") == True
assert sm.state == "idle"

try:
    sm.trigger("pause")
    assert False, "should have raised ValueError"
except ValueError:
    pass

sm2 = StateMachine("locked")
sm2.add_transition("locked", "unlock", "unlocked", guard=lambda ctx: ctx.get("pin") == 1234)
sm2.add_transition("locked", "unlock", "unlocked", guard=lambda ctx: ctx.get("key") == "master")

result = sm2.trigger("unlock", pin=9999)
assert result == False, f"wrong pin should not unlock: {result}"
assert sm2.state == "locked"

result = sm2.trigger("unlock", pin=1234)
assert result == True
assert sm2.state == "unlocked"

print("ALL TESTS PASSED")