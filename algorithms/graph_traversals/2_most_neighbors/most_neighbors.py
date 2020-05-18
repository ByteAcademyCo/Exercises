# A Graph is either:
# None
# Node

class Node:
    # val: int
    # log: listof(Graph)
    def __init__(self, val, log):
        self.val = val
        self.log = log

# Write a function called most_neighbors that consumes a Graph g and returns the Node with the most neighbors
# ie. most_neighbors(Node(1, [Node(2, [Node(3, None), Node(4, None), Node(5, None)]), Node(2, None), Node(10, [Node(5, None), Node(3, [Node(1, None)])])])) -> Node(2, [Node(3, None), Node(4, None), Node(5, None)])
def find_most_neighbors(log, most_neighbor):
    if log is None or len(log) == 0:
        return most_neighbor
    else:
        return max(helper(log[0], most_neighbor), find_most_neighbors(log[1:], most_neighbor))
def helper(g, most_neighbor):
    if g is None or g.log is None:
        return most_neighbor
    if len(g.log) > len(most_neighbor.log):
        return find_most_neighbors(g.log, g)
    else:
        return find_most_neighbors(g.log, most_neighbor)

def most_neighbors(g):
    return find_most_neighbors(g.log, g)

import pytest

def test_most_neighbors():
    graph = Node(100, [Node(2, [Node(3, None), Node(4, None), Node(5, None), Node(10, None), Node(15, None)]), Node(2, None), Node(10, [Node(5, None), Node(3, [Node(1, None)])])])
    g2 = Node(1, [Node(2, [Node(3, None), Node(4, None)])])
    assert most_neighbors(graph).val == 2
    assert len(most_neighbors(graph)) == 5

