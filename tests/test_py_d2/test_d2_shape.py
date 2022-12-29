# -*- coding: utf-8 -*-
from py_d2.D2Connection import D2Connection
from py_d2.D2Shape import D2Shape
from py_d2.D2Style import D2Style


def test_d2_shape():
    shape = D2Shape(name="shape_name")
    assert str(shape) == "shape_name"


def test_d2_shape_label():
    shape = D2Shape(name="shape_name", label="shape_label")
    assert str(shape) == "shape_name: shape_label"


def test_d2_shape_style():
    shape = D2Shape(name="shape_name", style=D2Style(fill="red"))
    assert str(shape) == "shape_name: {\n  style: {\n    fill: red\n  }\n}"


def test_d2_shape_container():
    shape = D2Shape(name="shape_name", label="container_label")
    shape.add_shape(D2Shape(name="shape_1"))
    shape.add_shape(D2Shape(name="shape_2"))
    shape.add_connection(D2Connection(from_shape="shape_1", to_shape="shape_2"))
    assert str(shape) == "\n".join(["shape_name: container_label {", "  shape_1", "  shape_2", "  shape_1 -> shape_2", "}"])


def test_d2_shape_container_style():

    shape = D2Shape(name="shape_name", label="container_label")
    shape.add_shape(D2Shape(name="shape_1", style=D2Style(fill="red")))
    shape.add_shape(D2Shape(name="shape_2"))
    shape.add_connection(D2Connection(from_shape="shape_1", to_shape="shape_2"))

    assert str(shape) == "\n".join(
        [
            "shape_name: container_label {",
            "  shape_1: {",
            "    style: {",
            "      fill: red",
            "    }",
            "  }",
            "  shape_2",
            "  shape_1 -> shape_2",
            "}",
        ]
    )


def test_d2_shape_container_in_container_with_shapes():

    shape = D2Shape(name="shape_name", label="container_label")
    shape.add_shape(
        D2Shape(
            name="shape_1",
            style=D2Style(fill="red"),
            shapes=[D2Shape(name="shape_2", style=D2Style(fill="blue")), D2Shape(name="shape_3")],
            connections=[D2Connection(from_shape="shape_2", to_shape="shape_3")],
        )
    )
    shape.add_shape(D2Shape(name="shape_4"))

    assert str(shape) == "\n".join(
        [
            "shape_name: container_label {",
            "  shape_1: {",
            "    shape_2: {",
            "      style: {",
            "        fill: blue",
            "      }",
            "    }",
            "    shape_3",
            "    shape_2 -> shape_3",
            "    style: {",
            "      fill: red",
            "    }",
            "  }",
            "  shape_4",
            "}",
        ]
    )
