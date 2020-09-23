# Stacks and Queues - Backspace Compare

## Motivation
Data structures organize the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. 

In stacks, elements are stored one over another, and these elements get removed in the reverse order of the arrival i.e. LIFO concept is followed. LIFO means Last in First out.

Stacks and Queues are implemented using Linked Lists

## Problem Description
Define a Python function `backspace_compare` that comsumes two strings `str1` and `str2` and returns `True` if they are equal when typed into empty text editors and `False` otherwise. The character `#` means a backspace character.
Hint1: Try to think whether a Stack or a queue may be a useful tool to solve this problem!
Hint2: You may find your previously defined magic methods or a new magic method useful for this question.
You may use the implementation of a stack or queue from the lecture slides.

## Example:
```
str1 = "ab#c"
str2 = "ad#c"
backspace_compare(str1, str2) == True

str1 = "a##c"
str2 = "#a#c"
backspace_compare(str1, str2) == True

str1 = "a#c"
str2 = "c#d"
backspace_compare(str1, str2) == False
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory