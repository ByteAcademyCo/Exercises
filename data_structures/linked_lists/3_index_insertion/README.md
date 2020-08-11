#  Index Insertion 

## Motivation
However, there are some downsides to the linked list as well.

Since each linked list item has to store the reference to the next item, some extra memory is required.
    
Unlike Arrays, where you can directly access an item, you cannot access a linked list item directly since the only information you have is the reference to the first item. In Big O terms, worst-case access time is O(n).

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

Define a method within class `linkedList` named `insert_at_index` which consumes two parameters `index` and `data`. The method inserts the data element at given index position in the linked_list. You may assume `index` is a valid index in the list.
Note - index starts from `1`

## Example
```
sample_LL = Node(5, Node(3, Node(-1, None)))
sample_LL.insert_at_index(2, 2)
sample_LL = Node(5, Node(2, Node(3, Node(-1, None)))

```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
