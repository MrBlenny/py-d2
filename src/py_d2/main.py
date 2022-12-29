# -*- coding: utf-8 -*-
from py_d2.D2Diagram import D2Diagram
from py_d2.D2Link import D2Link
from py_d2.D2Node import D2Node
from py_d2.D2Style import D2Style


def example():
    print("Contructing a simple graph...")
    nodes = [
        D2Node(name="node_name1", style=D2Style(fill="red")),
        D2Node(name="node_name2", style=D2Style(fill="blue")),
    ]
    links = [D2Link(from_node="node_name1", to_node="node_name2")]

    diagram = D2Diagram(nodes=nodes, links=links)

    print("Writing graph to file...")
    with open("graph.d2", "w") as f:
        f.write(str(diagram))
        print("Done! (graph.d2)")


if __name__ == "__main__":
    example()
