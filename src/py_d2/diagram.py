# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import List
from typing import Optional

from py_d2.connection import D2Connection
from py_d2.helpers import indent
from py_d2.helpers import indent_lines
from py_d2.shape import D2Shape


class Layer:
    def __init__(
        self,
        name: str,
        diagram: Optional["D2Diagram"] = None,
    ):
        self.name = name
        self.diagram = diagram or D2Diagram()

    def set_diagram(self, diagram: "D2Diagram"):
        self.diagram = diagram

    def lines(self, depth=1) -> List[str]:
        lines = self.diagram.lines()

        if len(lines) == 0:
            return []

        outer_indent_size = depth * 2
        inner_indent_size = outer_indent_size + 2

        # Wrap lines with layer { } and add indentation
        wrapped_lines = [
            indent(f"{self.name}: {{", outer_indent_size),
            *indent_lines(lines, inner_indent_size),
            indent("}", outer_indent_size),
        ]

        return wrapped_lines

    def __repr__(self) -> str:
        lines = self.lines()
        return "\n".join(lines)


class D2Diagram:
    def __init__(
        self,
        shapes: Optional[List[D2Shape]] = None,
        connections: Optional[List[D2Connection]] = None,
        layers: Optional[List[Layer]] = None,
    ):
        self.shapes = shapes or []
        self.connections = connections or []
        self.layers = layers or []

    def add_shape(self, shape: D2Shape):
        self.shapes.append(shape)

    def add_connection(self, connection: D2Connection):
        self.connections.append(connection)

    def add_layer(self, layer: Layer):
        self.layers.append(layer)

    def lines(self) -> List[str]:
        shapes = [str(shape) for shape in self.shapes]
        connections = [str(connection) for connection in self.connections]
        layers = [line for layer in self.layers for line in layer.lines() if layer.lines()]
        layers = ["layers: {"] + layers + ["}"] if layers else []

        return shapes + connections + layers

    def __repr__(self) -> str:
        lines = self.lines()
        return "\n".join(lines)
