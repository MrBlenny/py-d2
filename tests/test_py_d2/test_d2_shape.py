# -*- coding: utf-8 -*-
from py_d2.connection import D2Connection
from py_d2.shape import D2Shape
from py_d2.shape import D2Text
from py_d2.shape import Shape
from py_d2.style import D2Style


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
    shape.add_connection(D2Connection(shape_1="shape_1", shape_2="shape_2"))
    assert str(shape) == "\n".join(
        ["shape_name: container_label {", "  shape_1", "  shape_2", "  shape_1 -> shape_2", "}"]
    )


def test_d2_shape_container_style():
    shape = D2Shape(name="shape_name", label="container_label")
    shape.add_shape(D2Shape(name="shape_1", style=D2Style(fill="red")))
    shape.add_shape(D2Shape(name="shape_2"))
    shape.add_connection(D2Connection(shape_1="shape_1", shape_2="shape_2"))

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
            connections=[D2Connection(shape_1="shape_2", shape_2="shape_3")],
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


def test_d2_shape_shapes():
    shape_rectangle = D2Shape(name="shape_name", shape=Shape.rectangle)
    shape_rectangle = D2Shape(name="shape_name", shape=Shape.rectangle)
    shape_square = D2Shape(name="shape_name", shape=Shape.square)
    shape_page = D2Shape(name="shape_name", shape=Shape.page)
    shape_parallelogram = D2Shape(name="shape_name", shape=Shape.parallelogram)
    shape_document = D2Shape(name="shape_name", shape=Shape.document)
    shape_cylinder = D2Shape(name="shape_name", shape=Shape.cylinder)
    shape_queue = D2Shape(name="shape_name", shape=Shape.queue)
    shape_package = D2Shape(name="shape_name", shape=Shape.package)
    shape_step = D2Shape(name="shape_name", shape=Shape.step)
    shape_callout = D2Shape(name="shape_name", shape=Shape.callout)
    shape_stored_data = D2Shape(name="shape_name", shape=Shape.stored_data)
    shape_person = D2Shape(name="shape_name", shape=Shape.person)
    shape_diamond = D2Shape(name="shape_name", shape=Shape.diamond)
    shape_oval = D2Shape(name="shape_name", shape=Shape.oval)
    shape_circle = D2Shape(name="shape_name", shape=Shape.circle)
    shape_hexagon = D2Shape(name="shape_name", shape=Shape.hexagon)
    shape_cloud = D2Shape(name="shape_name", shape=Shape.cloud)
    shape_text = D2Shape(name="shape_name", shape=Shape.text)
    shape_code = D2Shape(name="shape_name", shape=Shape.code)
    shape_sql_table = D2Shape(name="shape_name", shape=Shape.sql_table)
    shape_image = D2Shape(name="shape_name", shape=Shape.image)
    shape_classs = D2Shape(name="shape_name", shape=Shape.classs)
    shape_sequence_diagram = D2Shape(name="shape_name", shape=Shape.sequence_diagram)

    assert str(shape_rectangle) == "shape_name: {\n  shape: rectangle\n}"
    assert str(shape_rectangle) == "shape_name: {\n  shape: rectangle\n}"
    assert str(shape_square) == "shape_name: {\n  shape: square\n}"
    assert str(shape_page) == "shape_name: {\n  shape: page\n}"
    assert str(shape_parallelogram) == "shape_name: {\n  shape: parallelogram\n}"
    assert str(shape_document) == "shape_name: {\n  shape: document\n}"
    assert str(shape_cylinder) == "shape_name: {\n  shape: cylinder\n}"
    assert str(shape_queue) == "shape_name: {\n  shape: queue\n}"
    assert str(shape_package) == "shape_name: {\n  shape: package\n}"
    assert str(shape_step) == "shape_name: {\n  shape: step\n}"
    assert str(shape_callout) == "shape_name: {\n  shape: callout\n}"
    assert str(shape_stored_data) == "shape_name: {\n  shape: stored_data\n}"
    assert str(shape_person) == "shape_name: {\n  shape: person\n}"
    assert str(shape_diamond) == "shape_name: {\n  shape: diamond\n}"
    assert str(shape_oval) == "shape_name: {\n  shape: oval\n}"
    assert str(shape_circle) == "shape_name: {\n  shape: circle\n}"
    assert str(shape_hexagon) == "shape_name: {\n  shape: hexagon\n}"
    assert str(shape_cloud) == "shape_name: {\n  shape: cloud\n}"
    assert str(shape_text) == "shape_name: {\n  shape: text\n}"
    assert str(shape_code) == "shape_name: {\n  shape: code\n}"
    assert str(shape_sql_table) == "shape_name: {\n  shape: sql_table\n}"
    assert str(shape_image) == "shape_name: {\n  shape: image\n}"
    assert str(shape_classs) == "shape_name: {\n  shape: class\n}"
    assert str(shape_sequence_diagram) == "shape_name: {\n  shape: sequence_diagram\n}"


def test_d2_shape_near():
    shape = D2Shape(name="shape_name", near="some_other_shape")
    assert str(shape) == "shape_name: {\n  near: some_other_shape\n}"


def test_d2_shape_other_properties():
    text = "Some text"
    shape = D2Shape(name="shape_name", thing=D2Text(text=text, formatting="md"))
    assert str(shape) == "\n".join(["shape_name: {", "  thing: |md", "    Some text", "  |", "}"])


def test_d2_shape_other_properties_multi_line():
    text = "\n".join(["multiline text", "like this", "works too"])
    shape = D2Shape(name="shape_name", thing=D2Text(text=text, formatting="md"))
    assert str(shape) == "\n".join(
        ["shape_name: {", "  thing: |md", "    multiline text", "    like this", "    works too", "  |", "}"]
    )


def test_d2_shape_other_properties_can_be_anything():
    text = "\n".join(["multiline text", "like this", "works too"])
    shape = D2Shape(
        name="shape_name",
        description=D2Text(text=text, formatting="md"),
        other_thing=D2Text(text=text, formatting="md"),
    )
    assert str(shape) == "\n".join(
        [
            "shape_name: {",
            "  description: |md",
            "    multiline text",
            "    like this",
            "    works too",
            "  |",
            "  other_thing: |md",
            "    multiline text",
            "    like this",
            "    works too",
            "  |",
            "}",
        ]
    )


def test_d2_shape_text_can_specify_pipe_count():
    text = "const iLoveTypescript = 1 || true;\nconst really = () => iLoveTypescript"
    shape = D2Shape(name="shape_name", code=D2Text(text=text, formatting="ts", pipes=3))
    assert str(shape) == "\n".join(
        [
            "shape_name: {",
            "  code: |||ts",
            "    const iLoveTypescript = 1 || true;",
            "    const really = () => iLoveTypescript",
            "  |||",
            "}",
        ]
    )
