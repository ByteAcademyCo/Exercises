# Perfect Binary Tree

## Motivation
Tree is a hierarchical data structure. Main uses of trees include maintaining hierarchical data, providing moderate access and insert/delete operations. Binary trees are special cases of tree where every node has at most two children.

A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level.

# Problem Description
Given the following Binary tree definition:

'''
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
'''
Define a function `closest_value` which consumes two arguments `node` and `target`. The function returns closest value of a given target value in a given non-empty Binary Search Tree (BST) of unique values. If `target` it equidistant from more than one node in the tree, your function should produce the node that comes first in a level order traversal of the tree.

# Example 
```
Input:
        6
      /   \
    4       10
  /  \    /   \
 3    5  8    12

root = Node(6)
root.left = Node(4)
root.right = Node(10)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(8)
root.right.right = Node(12)

closest_value(root, 7) == 6

```
## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory