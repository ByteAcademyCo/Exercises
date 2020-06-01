# Stack Delete Middle 

## Motivation
Delete middle element of a stack

Given a stack with push(), pop(), empty() operations, delete middle of it without using any additional data structure.

The idea is to use recursive calls. We first remove all items one by one, then we recur. After recursive calls, we push all items back except the middle item.

## Problem Description
Write a Python program to delete the middle element of a stack object `st` containing random string integer values. 
Your goal is to create a class based structure `Stack` containing different stack_operations.
Create a function `deletemid` which performs logic to delete the middle element of the stack `st`
Display the `result` of the remaining elements of the stack.

## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
