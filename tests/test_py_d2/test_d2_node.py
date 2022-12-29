# -*- coding: utf-8 -*-
from py_d2.D2Link import D2Link
from py_d2.D2Node import D2Node
from py_d2.D2Style import D2Style


def test_d2_node():
    node = D2Node(name="node_name")
    assert str(node) == "node_name"


def test_d2_node_labek():
    node = D2Node(name="node_name", label="node_label")
    assert str(node) == "node_name: node_label"


def test_d2_node_style():
    node = D2Node(name="node_name", style=D2Style(fill="red"))
    assert str(node) == "node_name: {\n  style: {\n    fill: red\n  }\n}"


def test_d2_node_container():
    node = D2Node(name="node_name", label="container_label")
    node.add_node(D2Node(name="node_1"))
    node.add_node(D2Node(name="node_2"))
    node.add_link(D2Link(from_node="node_1", to_node="node_2"))
    assert str(node) == "\n".join(["node_name: container_label {", "  node_1", "  node_2", "  node_1 -> node_2", "}"])


def test_d2_node_container_style():

    node = D2Node(name="node_name", label="container_label")
    node.add_node(D2Node(name="node_1", style=D2Style(fill="red")))
    node.add_node(D2Node(name="node_2"))
    node.add_link(D2Link(from_node="node_1", to_node="node_2"))

    assert str(node) == "\n".join(
        [
            "node_name: container_label {",
            "  node_1: {",
            "    style: {",
            "      fill: red",
            "    }",
            "  }",
            "  node_2",
            "  node_1 -> node_2",
            "}",
        ]
    )


def test_d2_node_container_in_container_with_nodes():

    node = D2Node(name="node_name", label="container_label")
    node.add_node(
        D2Node(
            name="node_1",
            style=D2Style(fill="red"),
            nodes=[D2Node(name="node_2", style=D2Style(fill="blue")), D2Node(name="node_3")],
            links=[D2Link(from_node="node_2", to_node="node_3")],
        )
    )
    node.add_node(D2Node(name="node_4"))

    assert str(node) == "\n".join(
        [
            "node_name: container_label {",
            "  node_1: {",
            "    node_2: {",
            "      style: {",
            "        fill: blue",
            "      }",
            "    }",
            "    node_3",
            "    node_2 -> node_3",
            "    style: {",
            "      fill: red",
            "    }",
            "  }",
            "  node_4",
            "}",
        ]
    )
