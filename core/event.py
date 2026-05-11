from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass(slots=True)
class Event:
    turn: int
    kind: str
    source: str
    target: Optional[str] = None
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "turn": self.turn,
            "kind": self.kind,
            "source": self.source,
            "target": self.target,
            "details": self.details,
        }

