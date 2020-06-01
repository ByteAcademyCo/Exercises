# Queue Reverse

## Motivation
Characteristics of Queue:

1. Insertion order of the queue is preserved.
2. Duplicacy is allowed.
3. Useful for parsing CPU task operations.

In this method, we will dequeue the elements from the Queue and push them into the Stack. Until the Queue becomes empty. Then we pop the elements from the Stack and enqueue them to the Queue till the stack is empty. As a result, the elements in the Queue will be reversed.

## Problem Description
Write a Python program that reverses the elements of a queue object `Q`
Your goal is to create 2 class based structures `Stack` and `Queue` having functions "empty check()","push()","pop()".
Perform the enqueue operation by pushing random integer values to the object `Q` and store the reversed elements in another stack object `S`. Call a function "Reverse" to return the list of reversed elements. 
Print the `result`.

## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
