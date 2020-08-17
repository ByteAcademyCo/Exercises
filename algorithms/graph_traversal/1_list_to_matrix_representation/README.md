# Adjacency List to Adjacency Matrix Representation

## Motivation
A Graph is a non-linear data structure consisting of nodes and edges. 
There are two common ways to represent a graph in python:

1. Adjacency Matrix Representation:
    Let n be the number of node in our graph.
    We can create an n by n matrix `M`, where `M[i][j] = 1` if there exists an edge from node `i` to node `j`. If there does not exist an edge from node `i` to node `j`, `M[i][j] = 0`

2. Adjacency List Representation:
    We can use a dictionary to represent a graph, where each key in the dictionary represents a node, and the values for each node `i` will be a list of all the nodes `j` where there exists an edge from node `i` to node `j`.
    
## Problem Description
Below is an adjacency list representation of a directed graph. The *solution.py* file contains a python dictionary
`adjacency_matrix`. Set the value of `adjacency_matrix` to be the adjacency matrix representation of the given dictionary, where each edge from node `i` to node `j` is represented by a value of `1` at position `ij` in your matrix.

```
adjacency_list = {
  0:  [0, 1, 3],
  1:  [3, 4],
  2:  [1],
  3:  [0, 2],
  4:  []
}
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
