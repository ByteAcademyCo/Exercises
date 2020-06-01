# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function named concatenate that consumes 2 LinkedLists ll1 and ll2. The function returns a LinkedList with all elements of ll1 followed by all elements in ll2.
# ie. concatenate(Node(1, Node(2, None)), Node(3, Node(4, None))) -> Node(1, Node(2, Node(3, Node(4, None))))
def concatenate(ll1, ll2):
    if ll1 == None:
        return ll2
    new_node = Node(ll1.first)
    new_node.rest = ll2 if ll1.rest == None else concatenate(ll1.rest, ll2)
    return new_node


