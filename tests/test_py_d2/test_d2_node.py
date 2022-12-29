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
    assert str(node) == "node_name: {\n  style: { \n    fill: red\n  }\n}"