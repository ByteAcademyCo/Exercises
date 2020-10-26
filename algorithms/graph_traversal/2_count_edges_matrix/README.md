# Count the Edges - Adjacency Matrix Representation

## Motivation
A Graph is a non-linear data structure consisting of nodes and edges. 
There are two common ways to represent a graph in python:

1. Adjacency Matrix Representation:
    Let n be the number of node in our graph.
    We can create an n by n matrix `M`, where `M[i][j] = 1` if there exists an edge from node `i` to node `j`. If there does not exist an edge from node `i` to node `j`, `M[i][j] = 0`

2. Adjacency List Representation:
    We can use a dictionary to represent a graph, where each key in the dictionary represents a node, and the values for each node `i` will be a list of all the nodes `j` where there exists an edge from node `i` to node `j`.
    
## Problem Description
In the *solution.py* file, define a function `count_edges` that consumes an adjacency matrix and returns the total
number of edges in the graph defined by the given matrix. A value of `1` at index `ij` represents an edge from node `i`
to node `j`.

## Example
```
matrix = [
    [0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0]
]
count_edges(matrix) == 10
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
