# -*- coding: utf-8 -*-
from __future__ import annotations

from enum import Enum
from typing import List
from typing import Optional

from py_d2.D2Connection import D2Connection
from py_d2.D2Style import D2Style
from py_d2.helpers import add_label_and_properties
from py_d2.helpers import flatten


class Shape(Enum):
    rectangle = "rectangle"
    square = "square"
    page = "page"
    parallelogram = "parallelogram"
    document = "document"
    cylinder = "cylinder"
    queue = "queue"
    package = "package"
    step = "step"
    callout = "callout"
    stored_data = "stored_data"
    person = "person"
    diamond = "diamond"
    oval = "oval"
    circle = "circle"
    hexagon = "hexagon"
    cloud = "cloud"
    text = "text"
    code = "code"
    sql_table = "sql_table"
    image = "image"
    classs = "class"
    sequence_diagram = "sequence_diagram"


class D2Shape:
    def __init__(
        self,
        name: str,
        label: Optional[str] = None,
        shape: Optional[Shape] = None,
        shapes: Optional[List[D2Shape]] = None,
        style: Optional[D2Style] = None,
        connections: Optional[List[D2Connection]] = None,
    ):
        self.name = name
        self.label = label
        self.shape = shape
        self.shapes = shapes or []
        self.style = style
        self.connections = connections or []

    def add_shape(self, shape: D2Shape):
        self.shapes.append(shape)

    def add_connection(self, connection: D2Connection):
        self.connections.append(connection)

    def lines(self) -> List[str]:
        shapes = flatten([shape.lines() for shape in self.shapes])
        connections = flatten([connection.lines() for connection in self.connections])
        properties = shapes + connections

        if self.shape:
            properties.append(f"shape: {self.shape.value}")

        if self.style:
            properties += self.style.lines()

        lines = add_label_and_properties(self.name, self.label, properties)

        return lines

    def __repr__(self) -> str:
        lines = self.lines()
        return "\n".join(lines)
