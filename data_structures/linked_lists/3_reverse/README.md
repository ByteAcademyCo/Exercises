#  Reverse Linked List

## Problem Description
Given the following Linked List definition:

A Linked List is either:
a) None
b) Node

```
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
```

Define a method within class `linkedList` named `reverse` that reverses the linkedList. The linked list should be mutated, and you should not create a new linkedList.

## Example
```
sample_LL = Node(5, Node(3, Node(-1, None)))
sample_LL.reverse()
sample_LL = Node(-1, Node(3, Node(5, None)))
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
