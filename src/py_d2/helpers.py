from typing import List


def indent(items: List[str], n: int = 2) -> List[str]:
    return [f"{' '*n}{item}" for item in items]


def lines(items: List[str], n: int = 2) -> str:
    return "\n".join(items)
