# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function called has_cycle that consumes a LinkedList ll and returns True if ll contains a cycle and False otherwise
# x = Node(1, Node(2, x))
# has_cycle(Node(1, Node(2, None))) -> False
# has_cycle(x) -> True
def has_cycle(ll):
    if ll == None or ll.rest == None:
        return False
    tortoise = ll
    hare = ll.rest
    while hare != None and hare.rest != None:
        if id(tortoise) == id(hare):
            return True
        else:
            tortoise = tortoise.next
            hare = hare.next.next
    return False

