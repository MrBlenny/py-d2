# -*- coding: utf-8 -*-
from typing import List
from typing import Optional


def indent(items: List[str], n: int = 2) -> List[str]:
    return [f"{' '*n}{item}" for item in items]


def add_label_and_properties(
    name: str, label: Optional[str] = None, properties: Optional[List[str]] = None
) -> List[str]:
    has_properties: bool = properties is not None and len(properties) > 0

    first_line = name
    if label or has_properties:
        first_line += ":"

    if label:
        first_line += f" {label}"

    if has_properties:
        first_line += " {"

    if properties and has_properties:
        return [first_line, *indent(properties), "}"]

    return [first_line]


def flatten(items: List[List[str]]) -> List[str]:
    return [item for sublist in items for item in sublist]
