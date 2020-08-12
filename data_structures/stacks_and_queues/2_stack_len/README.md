# Stack Magic Method - Length

## Motivation
Data structure organizes the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

In stacks, elements are stored one over another, and these elements get removed in the reverse order of the arrival i.e. LIFO concept is followed. LIFO means Last in First out.

A stack is implemented using Linked Lists

## Problem Description
Define a Python magic method `__len__` inside the `Stack` class that returns the length of the stack.
By defining this magic method, we can then use the shothand built in python len() on a stack object.

## Example:
```
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
len(stack1) => 3

stack2 = Stack()
len(stack2) => 0
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory