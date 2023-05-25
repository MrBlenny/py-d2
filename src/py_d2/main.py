# -*- coding: utf-8 -*-
from py_d2.connection import D2Connection
from py_d2.diagram import D2Diagram
from py_d2.shape import D2Shape
from py_d2.style import D2Style


def example():
    print("Contructing a simple graph...")
    shapes = [
        D2Shape(name="shape_name1", style=D2Style(fill="red")),
        D2Shape(name="shape_name2", style=D2Style(fill="blue")),
    ]
    connections = [D2Connection(shape_1="shape_name1", shape_2="shape_name2")]

    diagram = D2Diagram(shapes=shapes, connections=connections)

    print("Writing graph to file...")
    with open("graph.d2", "w", encoding="utf-8") as f:
        f.write(str(diagram))
        print("Done! (graph.d2)")


if __name__ == "__main__":
    example()
