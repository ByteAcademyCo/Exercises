# Stacks and Queues - Backspace Compare

## Motivation
Data structures organize the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. 

In stacks, elements are stored one over another, and these elements get removed in the reverse order of the arrival i.e. LIFO concept is followed. LIFO means Last in First out.

Stacks and Queues are implemented using Linked Lists

## Problem Description
Define a Python function `minimum_parenteses` that comsumes a string, `pstr` of open and close parentheses, `(` and `)`. Return the minimum number of parentheses needed to make the string valid. You may add `(` and `)` parentheses in any position in the string.
Hint1: You may find a Stack to be a useful tool to solve this problem!

## Example:
```
pstr = "()))(("
minimum_parentheses(pstr) == 4

pstr = "(("
minimum_parentheses(pstr) == 2

str = "(()())"
minimum_parentheses(pstr) == 0
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory