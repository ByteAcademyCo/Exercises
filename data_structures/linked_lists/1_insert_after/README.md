#  Insert After Data 


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
    def __init__(self, head=None):
        self.head = head
```

Define a method within class `linkedList` named `insert_after_item` that consumes two paraeters `x` and `data` and inserts an node with data `data` after the node in the linked_list with data `x`. If no node in the list has data `x`, insert the node with `data` at the end of the list.

## Example
```
sample_LL = Node(5, Node(3, Node(-1, None)))
sample_LL.insert_after_item(3, 0)
sample_LL == Node(5, Node(3, Node(0, Node(-1, None))))
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
