# Is Leaf Node

# Motivation
A Max-Heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.
A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node.
It is very useful is implementing priority queues where the queue item with higher weightage is given more priority in processing.
A node can be a terminal node, called Leaf or
A node can be a non-terminal node, called Node.

## Problem Description 
Given a heap, define a python function `is_leaf` that consumes two arguments `heap`, a list of integers, and `index`, an integer, and returns `True` if the element at `index` is leaf node and `False` otherwise.


## Example
is_leaf([1, 2, 3, 4, 5, 6], 3) == True
is_leaf([1, 2, 3, 4, 5, 6], 1) == False


## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory