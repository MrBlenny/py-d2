# -*- coding: utf-8 -*-
from enum import Enum
from typing import List
from typing import Optional


class Direction(Enum):
    TO = "->"
    FROM = "<-"
    BOTH = "<->"
    NONE = "--"


class D2Connection:
    def __init__(self, shape_1: str, shape_2: str, label: Optional[str] = None, direction: Direction = Direction.TO):
        self.shape_1 = shape_1
        self.shape_2 = shape_2
        self.label = label
        self.direction = direction

    def lines(self) -> List[str]:
        base = f"{self.shape_1} {self.direction.value} {self.shape_2}"
        if self.label:
            base += f": {self.label}"
        return [base]

    def __repr__(self) -> str:
        return "\n".join(self.lines())

    def __hash__(self):
        return hash((self.shape_1, self.shape_2, self.label, self.direction))

    def __eq__(self, other) -> bool:
        if ((self.shape_1, self.shape_2, self.direction, self.label) == (other.shape_1, other.shape_2, other.direction, other.label)):
            return True
        return False
