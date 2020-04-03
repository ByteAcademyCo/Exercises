# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function named remove that consumes a LinkedList ll and an integer index
# The function returns None and removes the element at the index specified
# Node(1, Node(2, Node(3, None))).remove(2) -> Node(1, Node(2, None))

def remove(ll, index):
    if ll != None:
        if index == 0:
            ll = ll.rest
        elif index == 1:
            if ll.rest != None:
                ll.rest = ll.rest.rest
        else:
            remove(ll.rest, index-1)
