# Depth First Search - Adjacency Matrix

## Motivation
A Graph is a non-linear data structure consisting of nodes and edges. 
There are two common ways to represent a graph in python:

1. Adjacency Matrix Representation:
    Let n be the number of node in our graph.
    We can create an n by n matrix `M`, where `M[i][j] = 1` if there exists an edge from node `i` to node `j`. If there does not exist an edge from node `i` to node `j`, `M[i][j] = 0`

2. Adjacency List Representation:
    We can use a dictionary to represent a graph, where each key in the dictionary represents a node, and the values for each node `i` will be a list of all the nodes `j` where there exists an edge from node `i` to node `j`.
    
## Problem Description
In the *solution.py* file, define a function `exists_path` that consumes 3 parameters, `adjacency_matrix` an adjacency
matrix representation of a graph, `origin` a number representing a node in the graph, and `destination` representing a
node in the graph. The function returns `True` if `destination` is reachable from `origin` and `False` otherwise. The function
returns `False` if either `origin` or `destination` is not contained in the given graph.

## Example
```
matrix = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0]
]

exists_path(matrix, 0, 2) == True
exists_path(matrix, 1, 0) == False
exists_path(matrix, 2, 4) == False
exists_path(matrix, 3, 0) == False
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
