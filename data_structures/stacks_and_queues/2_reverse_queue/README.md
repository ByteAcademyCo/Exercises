# Stacks and Queues - Backspace Compare

## Motivation
Data structures organize the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. 

In stacks, elements are stored one over another, and these elements get removed in the reverse order of the arrival i.e. LIFO concept is followed. LIFO means Last in First out.

Stacks and Queues are implemented using Linked Lists

## Problem Description
In the Queue class, define a method `reverse_queue` that reverses a queue and returns None. You may use a stack in the implementation of this method.
You may use the implementation of a stack and queue from the lecture slides.


## Example:
```
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

retqueue = Queue()
retqueue.enqueue(3)
retqueue.enqueue(2)
retqueue.enqueue(1)

queue.reverse_queue() == None
queue == retqueue
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory