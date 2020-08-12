# Stack Magic Method - Boolean

## Motivation
Data structure organizes the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

In stacks, elements are stored one over another, and these elements get removed in the reverse order of the arrival i.e. LIFO concept is followed. LIFO means Last in First out.

A stack is implemented using Linked Lists

## Problem Description
Define a Python magic method `__bool__` inside the `Stack` class that returns `False` if the stack is an empty stack and `True` otherwise.
By defining this magic method, we can then use the convenient shorthand notation `if stack: ...` or `while stack: ...` in python.

## Example:
```
stack1 = Stack()
stack1.push(1)
bool(stack1) => True

stack2 = Stack()
bool(stack2) => False
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory