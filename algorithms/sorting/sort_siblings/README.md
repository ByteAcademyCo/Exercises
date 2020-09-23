# Sort Siblings - Sorting Siblings by Age

## Motivation
Sorting is one of the most studied type of algorithms in computer science. There are many different sorting algorithms which may have different benifits and drawbacks given the problem you are trying to solve and your data. You must consider your time contraints and space constraints when choosing the appropriate sorting algorithm for your problem.
Sorting is important because it allows us to optimize data searching to a very high level, when data is stored in a sorted manner. Sorting also allows us to represent data in more readable formats.

## Problem Description
In the *solution.py* file, define a function `sort_siblings` that consumes a dictionary of siblings `sib_dict`, where the keys are the names of each sibling given as a string, and the value is the age of the sibling given as an integer. Output a list of sorted tuples `(name, age)` sorted in increasing order by age. If two siblings have the same age, sort them lexicographically. You may assume no two siblings have the same name.

## Example
```
sib_dict = {"Anton": 29,
            "Cosette": 3,
            "Nancy": 15,
            "Lucas": 15}

sort_siblings(sib_dict) == [("Cosette", 3), ("Lucas", 15), ("Nancy", 15), ("Anton", 29))]
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
