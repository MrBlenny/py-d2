from __future__ import annotations

from typing import List
from typing import Optional

from py_d2.D2Link import D2Link
from py_d2.D2Style import D2Style
from py_d2.helpers import add_label_and_properties
from py_d2.helpers import flatten


class D2Node:
    def __init__(
        self,
        name: str,
        label: Optional[str] = None,
        style: Optional[D2Style] = None,
        nodes: Optional[List[D2Node]] = None,
        links: Optional[List[D2Link]] = None,
    ):
        self.name = name
        self.label = label
        self.style = style
        self.nodes = nodes or []
        self.links = links or []

    # get the type of this class
    def add_node(self, node: D2Node):
        self.nodes.append(node)

    def add_link(self, link: D2Link):
        self.links.append(link)

    def lines(self) -> List[str]:
        nodes = flatten([node.lines() for node in self.nodes])
        links = flatten([link.lines() for link in self.links])
        properties = nodes + links

        if self.style:
            properties += self.style.lines()

        lines = add_label_and_properties(self.name, self.label, properties)

        return lines

    def __repr__(self) -> str:
        lines = self.lines()
        return "\n".join(lines)
