# Number of Hop Away - Adjacency List

## Motivation
A Graph is a non-linear data structure consisting of nodes and edges. 
There are two common ways to represent a graph in python:

1. Adjacency Matrix Representation:
    Let n be the number of node in our graph.
    We can create an n by n matrix `M`, where `M[i][j] = 1` if there exists an edge from node `i` to node `j`. If there does not exist an edge from node `i` to node `j`, `M[i][j] = 0`

2. Adjacency List Representation:
    We can use a dictionary to represent a graph, where each key in the dictionary represents a node, and the values for each node `i` will be a list of all the nodes `j` where there exists an edge from node `i` to node `j`.
    
## Problem Description
In the *solution.py* file, define a function `hops_away` that consumes 3 parameters, `adjacency_list` an adjacency list
representation of a graph, `node` a number representing a node in the graph, and `num_hops` a non-negative integer, and returns a list of
numbers representing the nodes that are exactly `num_hops` away from `node` in `adjacency_list`. The function returns an
empty list if `node` is not contained in the given graph.

## Example 
```
adj_list = {
    0: [1,3,5],
    1: [0,1,3,6],
    2: [],
    3: [0,3,5],
    4: [],
    5: [6],
    6: [3,5]
}

hops_away(adj_list, 0, 2) == [0, 1, 3, 6, 5]
hops_away(adj_list, 1, 0) == [1]
hops_away(adj_list, 7, 4) == []
hops_away(adj_list, 4, 3) == []
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
