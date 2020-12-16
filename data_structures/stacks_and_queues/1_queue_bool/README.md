# Queue Magic Method - Boolean

## Motivation
Data structures organize the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. 

A Queue is implemented using Linked Lists

## Problem Description
Define a Python magic method `__bool__` inside the `Queue` class that returns `False` if the queue is an empty queue and `True` otherwise.
By defining this magic method, we can then use the convenient shorthand notation `if queue: ...` or `while queue: ...` in python.

You may use the inplementation of a queue from the lecture slides.

## Example:
```
queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
bool(queue1) == True

queue2 = Queue()
bool(queue2) == False
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory