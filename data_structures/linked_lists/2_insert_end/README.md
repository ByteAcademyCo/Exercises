#  Insert Data End 

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


class linkedList:
    def __init__(self, head):
        self.head = head
```

Define a method within class `linkedList` named `insert_at_end` that consumes an integer `data` inserts a new node with `data` into the linked list at the end of the data structure. 

## Example
```
sample_LL = Node(5, Node(3, Node(-1, None)))
sample_LL.insert_at_end(40)
sample_LL == Node(5, Node(3, Node(-1, Node(40, None))))
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
