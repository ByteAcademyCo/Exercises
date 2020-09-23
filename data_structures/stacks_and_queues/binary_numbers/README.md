# Stacks and Queues - Backspace Compare

## Motivation
Data structures organize the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. 

In stacks, elements are stored one over another, and these elements get removed in the reverse order of the arrival i.e. LIFO concept is followed. LIFO means Last in First out.

Stacks and Queues are implemented using Linked Lists

## Problem Description
Define a Python function `binary_numbers` that comsumes a positive integer `n`, and returns a list of strings of all binary numbers from `1` to `n`.
Hint1: You may find a Queue to be a useful tool to solve this problem!

## Example:
```
binary_numbers(5) == ['1', '10', '11', '100', '101']
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory