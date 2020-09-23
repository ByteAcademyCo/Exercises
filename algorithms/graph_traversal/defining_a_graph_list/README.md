# Defining a Matrix - Graph Representation

## Motivation
A Graph is a non-linear data structure consisting of nodes and edges. 
There are two common ways to represent a graph in python:

1. Adjacency Matrix Representation:
    Let n be the number of node in our graph.
    We can create an n by n matrix `M`, where `M[i][j] = 1` if there exists an edge from node `i` to node `j`. If there does not exist an edge from node `i` to node `j`, `M[i][j] = 0`

2. Adjacency List Representation:
    We can use a dictionary to represent a graph, where each key in the dictionary represents a node, and the values for each node `i` will be a list of all the nodes `j` where there exists an edge from node `i` to node `j`.
    
## Problem Description
An island node is a node with no outgoing or incoming edges.
The *solution.py* file contains the variable `adjacency_list`. Set the value of `adjacency_list` to be a python dictionary representing an adjacency list. Define a graph with 4 total nodes and 4 total edges with nodes labelled from `0` to `3`. Node `0` should be an island node. There are many possible solutions.

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
