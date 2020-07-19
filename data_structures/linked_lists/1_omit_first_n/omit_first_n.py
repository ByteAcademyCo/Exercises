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

    def __len__(self) -> int:
        return 1 if self.rest is None else 1 + len(self.rest)


# Write a function called omit_first_n that consumes a LinkedList linked_list and an integer n. The function returns a LinkedList with the first n elements omitted or None if n > len(ll)
# omit_first_n(Node(1, Node(2, Node(3, None))), 2) -> Node(3, None)
def omit_first_n(linked_list: Optional[Node], n: int) -> Optional[Node]:
    return linked_list if n == 0 or linked_list is None else omit_first_n(linked_list.rest, n - 1)
