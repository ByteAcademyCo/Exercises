from typing import Optional

# A LinkedList is either:
# None
# Node


class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first: int, rest = None) -> None:
        self.first = first
        self.rest = rest
        self._length = 0

    def _calculate_length(self, node) -> int:
        self._length = 0 if node is None else 1 + self._calculate_length(node.rest)
        return self._length

    def __len__(self) -> int:
        return self._length if self._length else self._calculate_length(self)


# Write a function called omit_first_n that consumes a LinkedList linked_list and an integer n. The function returns a LinkedList with the first n elements omitted or None if n > len(ll)
# omit_first_n(Node(1, Node(2, Node(3, None))), 2) -> Node(3, None)
def omit_first_n(linked_list: Optional[Node], n: int) -> Optional[Node]:
    return linked_list if n == 0 or linked_list is None else omit_first_n(linked_list.rest, n - 1)


linked_list = Node(1, Node(2))
assert len(linked_list) == 2
assert omit_first_n(linked_list, 2) == None
