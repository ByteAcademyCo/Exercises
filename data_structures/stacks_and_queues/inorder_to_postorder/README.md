# Stacks and Queues - Backspace Compare

## Motivation
Data structures organize the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. 

In stacks, elements are stored one over another, and these elements get removed in the reverse order of the arrival i.e. LIFO concept is followed. LIFO means Last in First out.

Stacks and Queues are implemented using Linked Lists

## Problem Description
Define a Python function `inorder_to_postorder` that consues a string, `exp` which will be a mathematical expression in normal inorder notation, and returns a new string with `exp` represented in postorder notation. Note that in this question we will assume expressions are computed in the order of operands. You do not need to worry about the `BEDMAS` rules - (brackets, exponentials, division, multiplication, addition, substraction).
You may use the implementation of a stack and queue from the lecture slides.


## Example:
```
inorder_to_postorder("1+2*3") == "123+*"
inorder_to_postorder("1-2/3+4") == "1234-/+"
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory