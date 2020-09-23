# Number of Components - Adjacency List

## Motivation
A Graph is a non-linear data structure consisting of nodes and edges. 
There are two common ways to represent a graph in python:

1. Adjacency Matrix Representation:
    Let n be the number of node in our graph.
    We can create an n by n matrix `M`, where `M[i][j] = 1` if there exists an edge from node `i` to node `j`. If there does not exist an edge from node `i` to node `j`, `M[i][j] = 0`

2. Adjacency List Representation:
    We can use a dictionary to represent a graph, where each key in the dictionary represents a node, and the values for each node `i` will be a list of all the nodes `j` where there exists an edge from node `i` to node `j`.

## Problem Description
A component of an undirected graph is a subset of nodes. There must be a path between any two nodes in a component. There cannot be a path from inside the component to outside the component.

In the *solution.py* file, define a function `num_components` that consumes `adjacency_matrix` an adjacency matrix
representation of a graph, and returns the number of components in the graph. `adjacency_matrix` is guaranteed to be an
undirected graph, where all edges are bi-directional.

## Example
```
adjacency_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0]
]

num_components(adj_list) == 2
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
