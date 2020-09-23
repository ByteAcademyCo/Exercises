# Get the Value of Child Nodes

# Motivation
A Max-Heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.
A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node.
It is very useful is implementing priority queues where the queue item with higher weightage is given more priority in processing.

## Problem Description 
Given a Heap, define a python function `get_child_nodes` that consumes two arguments `heap`, a heap array, and `index` that returns the values of the children as a list `[left_child, right_child]` of the node at `index`. If `index` is not a valid index in the list return an empty list. If the node at `index` only has one child or no children, the list should just contain the one element or no elements respectively.

## Example
```
get_child_nodes([2, 3, 4, 5, 10], 0) == [3, 4]
get_child_nodes([2, 3, 4, 5, 10], 3) == []
get_child_nodes([2, 3, 4, 5, 10, 11], 2) == [11]
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory