# -*- coding: utf-8 -*-
from typing import List
from typing import Optional

from py_d2.D2Link import D2Link
from py_d2.D2Node import D2Node


class D2Diagram:
    def __init__(
        self,
        nodes: Optional[List[D2Node]] = None,
        links: Optional[List[D2Link]] = None,
    ):
        self.nodes = nodes or []
        self.links = links or []

    def add_node(self, node: D2Node):
        self.nodes.append(node)

    def add_link(self, link: D2Link):
        self.links.append(link)

    def __repr__(self) -> str:
        nodes = [str(node) for node in self.nodes]
        links = [str(link) for link in self.links]

        return "\n".join(nodes + links)
