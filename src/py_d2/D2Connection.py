# -*- coding: utf-8 -*-
from typing import List
from typing import Optional


class D2Connection:
    def __init__(self, from_shape: str, to_shape: str, label: Optional[str] = None):
        self.from_shape = from_shape
        self.to_shape = to_shape
        self.label = label

    def lines(self) -> List[str]:
        base = f"{self.from_shape} -> {self.to_shape}"
        if self.label:
            base += f": {self.label}"
        return [base]

    def __repr__(self) -> str:
        return "\n".join(self.lines())
