#  Delete Data End 

## Motivation
To delete an element from the end of the list, we simply have to iterate through the linked list till the second last element, and then we need to set the reference of the second last element to none, which will convert the second last element to last element.

## Problem Description
Given the following Linked List definition:

A Linked List is either:
a) None
b) Node

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self, head=None):
        self.head = head
```

Define a method within class `linkedlist` named `delete_end` that deletes the last node in the Linked List. 

## Example
```
sample_LL = Node(5, Node(3, Node(-1, None)))
sample_LL.delete_end()
sample_LL == Node(5, Node(3, None))
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
