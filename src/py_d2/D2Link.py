from typing import List
from typing import Optional


class D2Link:
    def __init__(self, from_node: str, to_node: str, label: Optional[str] = None):
        self.from_node = from_node
        self.to_node = to_node
        self.label = label

    def lines(self) -> List[str]:
        base = f"{self.from_node} -> {self.to_node}"
        if self.label:
            base += f": {self.label}"
        return [base]

    def __repr__(self) -> str:
        return "\n".join(self.lines())
