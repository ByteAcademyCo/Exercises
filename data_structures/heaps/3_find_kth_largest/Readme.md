# Find Median of a List

# Motivation
A Max-Heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.
A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node.
It is very useful when implementing priority queues where the queue item with higher weightage is given more priority in processing.

## Problem Description 
Define a python function `find_kth_largest` that consumes an argument `lst`, a non-empty unsorted list of integers, and an positive integer `k`, where `k <= len(lst)`, and using a MinHeap, return the `kth` largest value in `lst`.


## Example 
```
find_kth_largest([1, 2, 7, 6, 4], 2) == 6
find_kth_largest([1, 2, 5, 4, 9], 3) == 4
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory