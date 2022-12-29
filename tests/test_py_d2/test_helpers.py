# -*- coding: utf-8 -*-
from py_d2.helpers import add_label_and_properties


def test_add_label_and_properties():
    assert add_label_and_properties("shape_name", None, []) == ["shape_name"]
    assert add_label_and_properties("shape_name", "shape_label", []) == ["shape_name: shape_label"]
    assert add_label_and_properties("shape_name", None, ["style: {", "  fill: red", "}"]) == [
        "shape_name: {",
        "  style: {",
        "    fill: red",
        "  }",
        "}",
    ]
    assert add_label_and_properties("shape_name", "shape_label", ["style: {", "  fill: red", "}"]) == [
        "shape_name: shape_label {",
        "  style: {",
        "    fill: red",
        "  }",
        "}",
    ]
