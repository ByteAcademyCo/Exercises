# Preorder List

## Motivation
Algorithm Preorder(tree)-
1. Visit the root.
2. Traverse the left subtree, i.e., call Preorder(left-subtree)
3. Traverse the right subtree, i.e., call Preorder(right-subtree) 

# Problem Description
Given the following Binary tree definition:

'''
class Node: 
	def __init__(self,key=None,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
'''

Define a function `Preorder` which consumes one argument `root`. The function returns the preorder traversal of the given binary tree.

# Example
```
Input:
        6
      /   \
    4       7
  /   \
 3     5

items = Node(6)
items.left = Node(4)
items.right = Node(7)
items.left.left = Node(3)
items.left.right = Node(5)
Preorder(items) == [6, 4, 3, 5, 7]

```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory