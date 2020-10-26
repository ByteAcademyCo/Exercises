# Most Neighbours - Adjacency List

## Motivation
A Graph is a non-linear data structure consisting of nodes and edges. 
There are two common ways to represent a graph in python:

1. Adjacency Matrix Representation:
    Let n be the number of node in our graph.
    We can create an n by n matrix `M`, where `M[i][j] = 1` if there exists an edge from node `i` to node `j`. If there does not exist an edge from node `i` to node `j`, `M[i][j] = 0`

2. Adjacency List Representation:
    We can use a dictionary to represent a graph, where each key in the dictionary represents a node, and the values for each node `i` will be a list of all the nodes `j` where there exists an edge from node `i` to node `j`.
    
## Problem Description
Two nodes are neighbours if there is an edge going from one to the other.

In the *solution.py* file, define a function `most_neighbours` that consumes one parameter `adjacency_list` and returns a number representing the node that has the largest number of neighbours in the graph. In the result of a tie, the function should return the lowest numbered node.

## Example
```
adjacency_list = {
    0: [1,3,5],
    1: [0,1,3,6],
    2: [],
    3: [0,1,2,3],
    4: [],
    5: [4]
}

most_neighbours(adjacency_list) == 1
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
