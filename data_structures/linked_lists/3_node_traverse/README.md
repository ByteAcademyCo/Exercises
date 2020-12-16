#  Connect Node Traverse

## Motivation
Linked lists are one of the most commonly used data structures in any programming language.
Every node in a single linked list contains an item and reference to the next item and that's it.

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

Define a method within class `linkedList` named `traverse` that traverses through each element in the Linked_list, and prints out each element in the list, each on a new line.

## Example
```
sample_LL = Node(5, Node(3, Node(-1, None)))
sample_LL.traverse()
output
5
3
-1
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
