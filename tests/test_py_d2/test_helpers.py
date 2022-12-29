from py_d2.helpers import add_label_and_properties


def test_add_label_and_properties():
    assert add_label_and_properties("node_name", None, []) == ["node_name"]
    assert add_label_and_properties("node_name", "node_label", []) == ["node_name: node_label"]
    assert add_label_and_properties("node_name", None, ["style: {", "  fill: red", "}"]) == [
        "node_name: {",
        "  style: {",
        "    fill: red",
        "  }",
        "}",
    ]
    assert add_label_and_properties("node_name", "node_label", ["style: {", "  fill: red", "}"]) == [
        "node_name: node_label {",
        "  style: {",
        "    fill: red",
        "  }",
        "}",
    ]