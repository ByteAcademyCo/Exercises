# Get Value of Parent Node

# Motivation
A Max-Heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.
A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node.
It is very useful is implementing priority queues where the queue item with higher weightage is given more priority in processing.

## Problem Description 
Given a Heap, Define a python function `get_parent_node` that consumes two arguments `heap`, a heap array, and `index` that returns the value of parent node for the node at the given `index`. If `index` is the root node, return the value of the root. If `index` is not a valid index in the list return the string `"{index} is not a valid index in the heap"` where `{index}` is replaced by the number `index`.


## Example
```
get_parent_node([2,3,4,5,10], 4) == 3
get_parent_node([2,3,4,5,10], 0) == 2
get_parent_node([2,3,4,5,10], 5) == "5 is not a valid index in the heap"
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory