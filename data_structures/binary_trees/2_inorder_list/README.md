# Inorder List

## Motivation
Algorithm Inorder(tree)
1. Traverse the left subtree, i.e., call Inorder(left-subtree)
2. Visit the root.
3. Traverse the right subtree, i.e., call Inorder(right-subtree)

# Problem Description
Given the following Binary tree definition:

'''
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
'''

Define a function `Inorder` which consumes one argument `root`. The function returns the inorder traversal of a given binary tree.

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
Inorder(items) == [3, 4, 5, 6, 7]

```
## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory