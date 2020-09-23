# Stacks and Queues - Backspace Compare

## Motivation
Data structures organize the storage in computers so that we can easily access and change data. Stacks and Queues are the earliest data structure defined in computer science.

A Queue follows the First-in-First-Out (FIFO) principle. It is opened from both the ends hence we can easily add elements to the back and can remove elements from the front. 

In stacks, elements are stored one over another, and these elements get removed in the reverse order of the arrival i.e. LIFO concept is followed. LIFO means Last in First out.

Stacks and Queues are implemented using Linked Lists

## Problem Description
Define a Python function `reverse_words` that comsumes a string `sentence`, which is a string of words seperated by spaces. Return a string where the order of the words in `sentece` is reversed.
You may use the implementation of a stack or queue from the lecture slides.

## Example:
```
sentence = "hello bonjour aloha"
reverse_words(sentence) == "aloha bonjour hello"
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory