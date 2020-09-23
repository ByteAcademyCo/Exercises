# Insert node 

## Motivation
Given a binary tree and a key, insert the key into the binary tree at first position available in level order.

# Problem Description
Given the following Binary tree definition:

'''
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
'''

Define a methode `insert` inside the Node class which consumes two arguments `self` and `key`. The function inserts `key` into the binary tree at first position available in level order.


# Example
```
Input:
        6
      /   \
    11     9
   /      /  \
 7      15    8

items = Node(6)
items.left = Node(11)
items.right = Node(9)
items.left.left = Node(7)
items.right.left = Node(15)
items.right.right = Node(8)

items.insert(12)

output:
       10
      /   \
    11      9
   /  \    /  \
 7    12  15   8

```

items = Node(6)
items.left = Node(11)
items.right = Node(9)
items.left.left = Node(7)
items.right.left = Node(15)
items.right.right = Node(8)

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory