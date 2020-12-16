#  Delete Item Value

## Motivation
Deletion by Item Value

To delete the element by value, we first have to find the node that contains the item with the specified value and then delete the node. Finding the item with the specified value is pretty similar to searching the item. Once the item to be deleted is found, the reference of the node before the item is set to the node that exists after the item being deleted.

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

Define a method within class `linkedList` named `delete_item_by_value` that consumes one parameter `x`.The method deletes the specified data value from the linked_list. If `x` is not in the list, the list should remain unchanged.

## Example
```
sample_LL = Node(5, Node(3, Node(-1, None)))
sample_LL.delete_item_by_value(3)
sample_LL == Node(5, Node(-1, None))
```

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
