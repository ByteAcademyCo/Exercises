# nth Preorder 

## Motivation
Given the binary tree and you have to find out the N-th node from the Preorder traversal 
Input: n = 5
            
             25
           /    \
          20    30
        /    \ /   \
      18    22 24   32

Output: 30
 

# Problem Description
Given the following Binary tree definition:

'''
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
'''

Define a function `NthPreorder` which consumes two arguments `root`, a binary tree,and `n`, a non-negative integer. The function returns n-th node of a preorder traversal. If there are less than `n` elements in the tree `root` return the string `"no n-th element"` where `n` in the string is the number coresponding to the parameter `n`. 

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

Preorder Traversal = [5,6,8,9,7]

NthPreorder(items,3) == 8
NthPreorder(items,6) == "no 6-th element"
 ```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory