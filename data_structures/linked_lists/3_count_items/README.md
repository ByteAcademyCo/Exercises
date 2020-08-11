#  Count Data Items

## Motivation
A linked list is a dynamic data structure which means that the memory reserved for the link list can be increased or reduced at runtime. No memory is allocated for a linked list data structure in advance. Whenever a new item is required to be added to the linked, the memory for the new node is created at run time. On the other hand, in case of the array, memory has to be allocated in advance for a specific number of items. In cases where sufficient items are not available to fill all array index, memory space is wasted.

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

Define a method within class `linkedList` named `get_count` that returns the count of number of elements in the linked_list.

## Example
```
sample_LL = Node(5, Node(3, Node(-1, None)))
sample_LL.get_count() == 3
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
