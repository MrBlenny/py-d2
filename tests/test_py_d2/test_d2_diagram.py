# -*- coding: utf-8 -*-
from py_d2.D2Connection import D2Connection
from py_d2.D2Diagram import D2Diagram
from py_d2.D2Shape import D2Shape
from py_d2.D2Style import D2Style


def test_d2_diagram():
    diagram = D2Diagram()
    assert str(diagram) == ""


def test_d2_diagram_one_shape():
    diagram = D2Diagram()
    diagram.add_shape(D2Shape(name="shape_name"))
    assert str(diagram) == "shape_name"


def test_d2_diagram_two_shapes():
    shapes = [D2Shape(name="shape_name1"), D2Shape(name="shape_name2")]
    diagram = D2Diagram(shapes=shapes)
    assert str(diagram) == "\n".join(["shape_name1", "shape_name2"])


def test_d2_diagram_one_connection():
    shapes = [D2Shape(name="shape_name1"), D2Shape(name="shape_name2")]
    connections = [D2Connection(from_shape="shape_name1", to_shape="shape_name2")]

    diagram = D2Diagram(shapes=shapes, connections=connections)
    assert str(diagram) == "\n".join(["shape_name1", "shape_name2", "shape_name1 -> shape_name2"])


def test_d2_diagram_one_connection_imperative_connection():
    diagram = D2Diagram()
    diagram.add_shape(D2Shape(name="shape_name1"))
    diagram.add_shape(D2Shape(name="shape_name2"))
    diagram.add_connection(D2Connection(from_shape="shape_name1", to_shape="shape_name2"))
    assert str(diagram) == "\n".join(["shape_name1", "shape_name2", "shape_name1 -> shape_name2"])


def test_d2_diagram_one_connection_with_style():
    shapes = [
        D2Shape(name="shape_name1", style=D2Style(fill="red")),
        D2Shape(name="shape_name2", style=D2Style(fill="blue")),
    ]
    connections = [D2Connection(from_shape="shape_name1", to_shape="shape_name2")]

    diagram = D2Diagram(shapes=shapes, connections=connections)
    assert str(diagram) == "\n".join(
        [
            "shape_name1: {",
            "  style: {",
            "    fill: red",
            "  }",
            "}",
            "shape_name2: {",
            "  style: {",
            "    fill: blue",
            "  }",
            "}",
            "shape_name1 -> shape_name2",
        ]
    )
