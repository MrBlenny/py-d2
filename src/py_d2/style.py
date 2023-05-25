# -*- coding: utf-8 -*-
from typing import List
from typing import Optional

from py_d2.helpers import add_label_and_properties


def stringify_bool(val: bool) -> str:
    return "true" if val else "false"


class D2Style:
    def __init__(
        self,
        stroke: Optional[str] = None,
        stroke_width: Optional[int] = None,
        fill: Optional[str] = None,
        shadow: Optional[bool] = None,
        opacity: Optional[float] = None,
        stroke_dash: Optional[int] = None,
        three_d: Optional[bool] = None,
    ):
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.fill = fill
        self.shadow = shadow
        self.opacity = opacity
        self.stroke_dash = stroke_dash
        self.three_d = three_d

    def lines(self) -> List[str]:
        styles: List[str] = []

        if self.stroke:
            styles.append(f"stroke: {self.stroke}")

        if self.stroke_width:
            styles.append(f"stroke-width: {self.stroke_width}")

        if self.fill:
            styles.append(f"fill: {self.fill}")

        if self.shadow:
            styles.append(f"shadow: {stringify_bool(self.shadow)}")

        if self.opacity:
            styles.append(f"opacity: {self.opacity}")

        if self.stroke_dash:
            styles.append(f"stroke-dash: {self.stroke_dash}")

        if self.three_d:
            styles.append(f"3d: {stringify_bool(self.three_d)}")

        if len(styles) == 0:
            return []

        return add_label_and_properties("style", None, styles)

    def __repr__(self) -> str:
        lines = self.lines()
        return "\n".join(lines)
