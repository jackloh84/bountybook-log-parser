"""StateMachine with transitions and guards.

- add_transition(from_state, event, to_state, guard=None)
- trigger(event, **ctx) -> bool  (True if transition fired)
- raises ValueError if event has no transitions from current state
"""
from collections import defaultdict


class StateMachine:
    def __init__(self, initial_state: str):
        self._state = initial_state
        # transitions[(from_state, event)] -> list of (to_state, guard|None)
        self._transitions: dict[tuple[str, str], list[tuple[str, "callable | None"]]] = defaultdict(list)

    @property
    def state(self) -> str:
        return self._state

    def add_transition(self, from_state: str, event: str, to_state: str, guard=None) -> None:
        self._transitions[(from_state, event)].append((to_state, guard))

    def trigger(self, event: str, **ctx) -> bool:
        key = (self._state, event)
        if key not in self._transitions or not self._transitions[key]:
            raise ValueError(f"No transition from '{self._state}' on event '{event}'")
        # Try each candidate transition; first whose guard passes wins
        for to_state, guard in self._transitions[key]:
            if guard is None:
                self._state = to_state
                return True
            try:
                passes = bool(guard(ctx))
            except Exception:
                passes = False
            if passes:
                self._state = to_state
                return True
        # All guards failed → treat as no-op (return False)
        return False