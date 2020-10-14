# Python Caches

## Motivation
The ``id`` function helps us determine the memory address of a particular variable. Python dynamically creates memory each time we create a variable. For example, if you type the following code into a Python command prompt, you will see the memory address of where x and y are stored. Notice how they change upon changing the variables - this is Python's dynamic nature of memory creation. **Note: Do not type this in an editor - reasons beyond the scope of this lesson**.
```Python
>>> x = 1
>>> y = 1
>>> id(x)
10914496
>>> id(y)
10914496
>>> x = 1234
>>> id(x)
1400159191253392
>>> y = 1234
>>> id(y)
1400159191254216
```

You will notice that when x and y are 1, they are stored in the same memory address while when x and y are 1234, they are stored in separate memory addresses. This is attributed to the fact that Python only dynamically creates integers above a certain range and stores small integers in memory as they are commonly used in a developers code. This is known as [caching](https://en.wikipedia.org/wiki/Cache_(computing)) and it improves the performance of Python code as dynamically creating memory is expensive. 

## Problem Descripton

Your goal is to determine what range of integers Python saves in memory (caches).

* a) What is the lower bound of the range?
* b) What is the upper bound of the range?

## Testing
* To test your solution, type 'pytest' within the **Solutions** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
* The file contains 2 variables - `LOWER_BOUND` and `UPPER_BOUND representing each bound respectively
* Overwrite these numbers with your answers
