# Complete Binary tree

## Motivation
Binary Tree is a complete Binary Tree if all the levels are completely filled except possibly the last level and the last level has all keys as left as possible

# Problem Description
Given the following Binary tree definition:

'''
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
'''


Define a function `height` which consumes one argument `node`. The function returns height of a tree.(the number of nodes along the longest path from the root node down to the farthest leaf node)

# Example 
```
Input:
        6
      /   \
    4       7
  /   \
 3     5
 
output: 3

```
## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory