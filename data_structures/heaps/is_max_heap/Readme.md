# Is Max Heap

# Motivation
A Max-Heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.
A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node.
It is very useful when implementing priority queues where the queue item with higher weightage is given more priority in processing.

## Problem Description 
Define a python function `is_max_heap` that consumes a list `lst`, and returns `True` if lst is in the order of a valid maxHeap and `False` otherwise. 
Recall in a maxHeap:
* The root will be at `lst[0]`
* The Parent of `lst[i]` will be at `lst[(i-1)/2]`
* The left child of `lst[i]` will be at `lst[(2*i)+1]`
* The right child of `lst[i]` will be at `lst[(2*i)+2]`

## Example 
```
is_min_heap([1, 2, 3, 7, 6, 4, 5]) == False
is_min_heap([5, 3, 4, 1, 2]) == True
is_min_heap([]) == True
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory