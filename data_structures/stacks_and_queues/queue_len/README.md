# Queue Magic Method - Length

## Motivation
Data structures organize the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. 

A Queue is implemented using Linked Lists

## Problem Description
Define a Python magic method `__len__` inside the `Queue` class that returns the length of the queue.
By defining this magic method, we can then use the shothand built in python len() on a queue object.

You may use the inplementation of a queue from the lecture slides.


## Example:
```
queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
len(queue1) == 3

queue2 = Queue()
len(queue2) == 0
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory