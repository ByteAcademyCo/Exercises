# A Graph is either:
# None
# Node

class Node:
    # val: int
    # log: listof(Graph)
    def __init__(self, val, log):
        self.val = val
        self.log = log

# Write a function called len that consumes a Graph g and returns the number of Nodes in the graph
# ie. length(Node(1, [Node(2, None), Node(3, [Node(4, None)])])) -> 4
def length(graph):
    ...
