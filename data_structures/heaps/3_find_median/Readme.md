# Complete Binary Tree

# Motivation
A Max-Heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.
A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node.
It is very useful when implementing priority queues where the queue item with higher weightage is given more priority in processing.

## Problem Description 
Define a python function `find_median` that consumes an argument `lst`, a non-empty unsorted list of integers, and using a MinHeap, return the median of `lst`. If the length of `lst` is even, return the larger of the two values.


## Example 
```
find_median([1, 2, 3, 7, 6, 4, 5]) => 4
find_median([5, 1]) => 5
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory