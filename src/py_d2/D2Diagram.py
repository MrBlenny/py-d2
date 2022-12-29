# -*- coding: utf-8 -*-
from typing import List
from typing import Optional

from py_d2.D2Connection import D2Connection
from py_d2.D2Shape import D2Shape


class D2Diagram:
    def __init__(
        self,
        shapes: Optional[List[D2Shape]] = None,
        connections: Optional[List[D2Connection]] = None,
    ):
        self.shapes = shapes or []
        self.connections = connections or []

    def add_shape(self, shape: D2Shape):
        self.shapes.append(shape)

    def add_connection(self, connection: D2Connection):
        self.connections.append(connection)

    def __repr__(self) -> str:
        shapes = [str(shape) for shape in self.shapes]
        connections = [str(connection) for connection in self.connections]

        return "\n".join(shapes + connections)
