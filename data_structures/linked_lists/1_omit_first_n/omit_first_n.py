# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function called omit_first_n that consumes a LinkedList ll and an integer n. The function returns a LinkedList with the first n elements omitted or None if n > len(ll)
# omit_first_n(Node(1, Node(2, Node(3, None))), 2) -> Node(3, None)
def omit_first_n(ll, n):
    if n == 0:
        return ll
    elif ll == None:
        return None
    else:
        return omit_first_n(ll.rest, n-1)
