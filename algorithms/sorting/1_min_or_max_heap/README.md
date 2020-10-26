# Heap Sort - Min or Max Heap

## Motivation
Sorting is one of the most studied type of algorithms in computer science. There are many different sorting algorithms which may have different benifits and drawbacks given the problem you are trying to solve and your data. You must consider your time contraints and space constraints when choosing the appropriate sorting algorithm for your problem.
Sorting is important because it allows us to optimize data searching to a very high level, when data is stored in a sorted manner. Sorting also allows us to represent data in more readable formats.

## Problem Description
In the *solution.py* file, define a function `min_or_max_heap` that consumes a heap of integers `heap`, and returns the string `"min"` if `heap` is a min heap, `max` if `heap` is a max heap and `"neither"` if the heap is neither a min nor a max heap. If `heap` satisfies the properties of both min and max heap, you may return either `"min"` or `"max"`. Recall a min heap is a tree structure such that each node is smaller than its child nodes and a max heap is a tree structue such that each node is larger than its child nodes. In python we will represent the heap `heap` as an array where the root of the tree is at index `0`, and for the `ith` node, `heap[(i-1)/2]` will be the parent of `heap[i]`, `heap[(2*i)+1]` will be the left child of `heap[i]`, and `heap[(2*i)+2]` will be the right child of `heap[i]`. 

## Example
```
heap = [1, 3, 6, 7, 9, 8]
min_or_max_heap(heap) == "min"

heap = [10, 5, 9, 4, 2, 8]
min_or_max_heap(heap) => "max"

heap = [10, 5, 8, 4, 2, 9]
min_or_max_heap(heap) => "neither"
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
