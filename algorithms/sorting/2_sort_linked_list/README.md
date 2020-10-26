# Linked Lists - Sort a Linked List

## Motivation
Sorting is one of the most studied type of algorithms in computer science. There are many different sorting algorithms which may have different benifits and drawbacks given the problem you are trying to solve and your data. You must consider your time contraints and space constraints when choosing the appropriate sorting algorithm for your problem.
Sorting is important because it allows us to optimize data searching to a very high level, when data is stored in a sorted manner. Sorting also allows us to represent data in more readable formats.

## Problem Description
In the *solution.py* file, define a method `sort_ll` inside the LinkedList class that sorts a linked list using your prefered sorting method. 
```
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def sort_ll(self):
        return

class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None
```

## Example
```
n1 = ListNode(5)
n2 = ListNode(6, n1)
n3 = ListNode (4, n2)
n4 = ListNode(1, n3)
llst = LinkedList(n4)

r1 = ListNode(6)
r2 = ListNode(5, r1)
r3 = ListNode(4, r2)
r4 = ListNode(1, r3)
returnlst = LinkedList(r4)

llst.sort_ll() == returnlst
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
