# Postorder List

## Motivation
Algorithm Postorder(tree)-
1. Traverse the left subtree, i.e., call Postorder(left-subtree)
2. Traverse the right subtree, i.e., call Postorder(right-subtree)
3. Visit the root.

# Problem Description
Given the following Binary tree definition:

'''
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
'''

Define a function `Postorder` which consumes one argument `root`. The function returns the postorder traversal of the given binary tree.

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
Postorder(items) == [3, 5, 4, 7, 6]
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory