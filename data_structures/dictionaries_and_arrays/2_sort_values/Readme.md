# Sort Values 

# Motivation
Dictionaries in Python are unsorted. They are stored by the hash value of the key, and this allows for fast lookup.

Operator.itemgetter() takes keys of dictionaries and converts them into tuples which is then sorted.The `operator` module has to be imported for its working

## Problem Description 
Define a Python function named `sort_dict` that consumes one parameter `my_dictionary`. The function returns the dictionary with sorted values.

## Examples
```
my_dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sort_dict(my_dictionary) = {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory