# nth Inorder 

## Motivation
Given the binary tree and you have to find out the n-th node of inorder traversal.
Input :  n = 3
```
            7
          /   \
         2     3
             /   \
            8     5
```
Output : 8
Inorder: 2 7 8 3 5
3rd node is 8

# Problem Description
Given the following Binary tree definition:

'''
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
'''

Define a function `NthInorder` which consumes two arguments `root`, a binary tree,and `n`, a non-negative integer. The function returns n-th node of inorder traversal. If there are less than `n` elements in the tree `root` return the string `"no n-th element"` where `n` in the string is the number coresponding to the parameter `n`. 

# Example
```
Input:
        5
      /   \
    6       7
  /   \
 8     9

items = Node(5)
items.left = Node(6)
items.right = Node(7)
items.left.left = Node(8)
items.left.right = Node(9)

Inorder Traversal = [8,6,9,5,7]

NthInorder(items,4) == 5
NthInorder(items,6) == "no 6-th element"

```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory