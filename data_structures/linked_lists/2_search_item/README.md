#  Search Item Exists

## Motivation
Since arrays require contiguous memory locations, it is very difficult to remove or insert an item in an array since the memory locations of a large number of items have to be updated. On the other hand, linked list items are not stored in a contiguous memory location, therefore you can easily update linked lists.

Owing to its flexibility, a linked list is more suitable for implementing data structures like stacks, queues, and lists.

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
    def __init__(self, head):
        self.head = head
```

Define a method within class `linkedList` named `search` that consumes one parameter `x`.The method returns `True` if the given item `x` exists in the Linked_list and `False` otherwise.

## Example
```
sample_LL = Node(5, Node(3, Node(-1, None)))
sample_LL.search(3) == True
sample_LL.search(0) == False
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
