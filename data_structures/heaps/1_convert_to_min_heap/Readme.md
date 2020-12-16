# Convert to Min Heap

# Motivation
A Max-Heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.
A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node.
It is very useful when implementing priority queues where the queue item with higher weightage is given more priority in processing.


## Problem Description 
Define a python function `convert_to_minHeap` that consumes an argument `tree`, a complete binary tree, and converts `tree` to a min heap and return the heap. Add nodes one at a time to your min heap using a preorder traversal of `tree`.


## Example 
```
        7
      /   \
    3       6
  /   \    /  \
 1     2  4    5

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3, n1, n2)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6, n4, n5)
n7 = TreeNode(7, n3, n6)
tree = Tree(n7)

convert_to_minHeap(tree) == MinHeap([1, 2, 3, 7, 6, 4, 5])
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory