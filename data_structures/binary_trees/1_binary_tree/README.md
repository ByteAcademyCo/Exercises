# Binary Tree 

## Motivation
A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child. Unlike Arrays, Linked Lists, Stack and queues, which are linear data structures, trees are hierarchical data structures.
We can define a binary tree (BT) to contain the following parts:
1. Key (of any type or None)
2. Left (of type None or BT)
3. Right (of Type None or BT)

# Problem Description
Define a python class `Node` constructor having arguments `key` representing the individual node data and `left` and `right`representing the respective children. The argumets should default to `None` if no values are given for `key`, `left`, and `right`.
Create a tree in object `sample_tree` with 5 as the root node key, 4 as the key of the left child and 7 as the key of the right child. 

# Example
```
Output:
        5
      /   \
     4     7

```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
