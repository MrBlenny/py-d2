# -*- coding: utf-8 -*-
from py_d2.D2Connection import D2Connection
from py_d2.D2Diagram import D2Diagram
from py_d2.D2Shape import D2Shape
from py_d2.D2Style import D2Style


def example():
    print("Contructing a simple graph...")
    shapes = [
        D2Shape(name="shape_name1", style=D2Style(fill="red")),
        D2Shape(name="shape_name2", style=D2Style(fill="blue")),
    ]
    connections = [D2Connection(shape_1="shape_name1", shape_2="shape_name2")]

    diagram = D2Diagram(shapes=shapes, connections=connections)

    print("Writing graph to file...")
    with open("graph.d2", "w") as f:
        f.write(str(diagram))
        print("Done! (graph.d2)")


if __name__ == "__main__":
    example()
