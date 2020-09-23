#  Insert Data Start

## Motivation
Depending upon the location where you want to insert an item, there are different ways to insert items in a single linked list.

Inserting Items at the Beginning-
The simplest way to insert an item in a single linked list is to add an item at the start of the list.

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

Define a method within class `linkedlist` named `insert_at_start` that consumes an integer `data` and inserts a node with `data` into the linked list at the start of the data structure.

## Example
```
sample_LL = Node(5, Node(3, Node(-1, None)))
sample_LL.insert_at_start(50)
sample_LL == Node(50, Node(5, Node(3, Node(-1, None))))
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
