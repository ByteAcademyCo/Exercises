# Search Node 

## Motivation
Let a binary search tree (BST) is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Unlike linear data structures (Array, Linked List, Queues, Stacks, etc) which have only one logical way to traverse them, trees can be traversed in different ways.
1. Inorder
2. Preorder 
3. Postorder 

# Problem Description
Given the following Binary tree definition:

'''
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
'''

Define a function `search` which consumes two arguments `root` and `key`. The function returns `True` if `key` is in the tree `root` and `False` otherwise.

# Example
```
        6
      /   \
    4       9
  /   \    /  \
 3     5  7   11

items = Node(6)
items.left = Node(4)
items.right = Node(9)
items.left.left = Node(3)
items.left.right = Node(5)
items.right.left = Node(7)
items.right.right = Node(11)

search(items,11) == True
search(items,8) == False

```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory