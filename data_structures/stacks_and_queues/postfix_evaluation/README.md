# Stacks and Queues - Backspace Compare

## Motivation
Data structures organize the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. 

In stacks, elements are stored one over another, and these elements get removed in the reverse order of the arrival i.e. LIFO concept is followed. LIFO means Last in First out.

Stacks and Queues are implemented using Linked Lists

## Problem Description
Define a Python function `postfix_eval` that comsumes a string, `exp` which is a string of integers followed by operators. This is a mathematical expression in postfix notation. Return the postfix evaluation of the expression.
Hint1: You may find a Queue to be a useful tool to solve this problem!

## Example:
```
exp = "123+*"
postfix_eval(exp) == 9 
1+2 = 3
3*3 = 9

exp = "1223+*/"
postfix_eval(exp) == 3 
1+2 = 3
3*2 = 6
6/2 = 3
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory