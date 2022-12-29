from typing import List
from typing import Optional

from py_d2.D2Style import D2Style
from py_d2.helpers import indent


class D2Node:
    def __init__(self, name: str, label: Optional[str] = None, style: Optional[D2Style] = None):
        self.name = name
        self.label = label
        self.style = style

    def lines(self) -> List[str]:
        first_line = self.name

        properties = []

        if self.style:
            styles = indent(self.style.lines())
            properties += styles

        has_properties = len(properties) > 0

        if self.label or has_properties:
            first_line += ":"

        if self.label:
            first_line += f" {self.label}"

        if has_properties:
            first_line += " {"

        if not self.style:
            return [first_line]

        return [first_line, *properties, "}"]

    def __repr__(self) -> str:
        lines = self.lines()
        return "\n".join(lines)
