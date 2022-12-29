from py_d2.D2Diagram import D2Diagram
from py_d2.D2Link import D2Link
from py_d2.D2Node import D2Node
from py_d2.D2Style import D2Style


def test_d2_diagram():
    diagram = D2Diagram()
    assert str(diagram) == ""

def test_d2_diagram_one_node():
    diagram = D2Diagram()
    diagram.add_node(D2Node(name="node_name"))
    assert str(diagram) == "node_name"

def test_d2_diagram_two_nodes():
    nodes = [D2Node(name="node_name1"), D2Node(name="node_name2")]
    diagram = D2Diagram(nodes=nodes)
    assert str(diagram) == "\n".join(["node_name1", "node_name2"])

def test_d2_diagram_one_link():
    nodes = [D2Node(name="node_name1"), D2Node(name="node_name2")]
    links = [D2Link(from_node="node_name1", to_node="node_name2")]

    diagram = D2Diagram(nodes=nodes, links=links)
    assert str(diagram) == "\n".join(["node_name1", "node_name2", "node_name1 -> node_name2"])

def test_d2_diagram_one_link_with_style():
    nodes = [D2Node(name="node_name1", style=D2Style(fill="red")), D2Node(name="node_name2", style=D2Style(fill="blue"))]
    links = [D2Link(from_node="node_name1", to_node="node_name2")]

    diagram = D2Diagram(nodes=nodes, links=links)
    assert str(diagram) == """node_name1: {
  style: { 
    fill: red
  }
}
node_name2: {
  style: { 
    fill: blue
  }
}
node_name1 -> node_name2"""
