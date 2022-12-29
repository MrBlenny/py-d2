# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import List
from typing import Optional

from py_d2.D2Connection import D2Connection
from py_d2.D2Style import D2Style
from py_d2.helpers import add_label_and_properties
from py_d2.helpers import flatten


class D2Shape:
    def __init__(
        self,
        name: str,
        label: Optional[str] = None,
        style: Optional[D2Style] = None,
        shapes: Optional[List[D2Shape]] = None,
        connections: Optional[List[D2Connection]] = None,
    ):
        self.name = name
        self.label = label
        self.style = style
        self.shapes = shapes or []
        self.connections = connections or []

    # get the type of this class
    def add_shape(self, shape: D2Shape):
        self.shapes.append(shape)

    def add_connection(self, connection: D2Connection):
        self.connections.append(connection)

    def lines(self) -> List[str]:
        shapes = flatten([shape.lines() for shape in self.shapes])
        connections = flatten([connection.lines() for connection in self.connections])
        properties = shapes + connections

        if self.style:
            properties += self.style.lines()

        lines = add_label_and_properties(self.name, self.label, properties)

        return lines

    def __repr__(self) -> str:
        lines = self.lines()
        return "\n".join(lines)
