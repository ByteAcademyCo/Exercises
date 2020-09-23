# Dynamic Programming Recursion - Knapsack Problem

## Motivation
We use Dynamic Programming algorithms when we have overlapping subproblems. If we have a naive recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. We can store the results of the subproblems, so that we do not have to re-compute them when needed later.
Dynamic programing can optimize the time complexity of a problem from exponential `O(2^n)` to polynomial `O(n^c)`, for some constant `c`.

## Problem Description
You are going on a camping trip and you have a knapsack you wish to pack with a weight capacity of `x` lbs. You are given a dictiomary where the keys are strings containing the names of items which you wish bring on your trip, which are mapped to a touple, containing the value of the given item and weight in lbs of the given item. The higher the value of the item, the more important it is to you to bring on your trip.

In the *solution.py* file, using dynamic programming, define a function `knap_sack` that consumes a positive integer `x` and a dictionary `items`, and returns the maximal value of items you can bring in your knapsack without exceeding the maximal capacity `x`. 

## Example
```
items = {"hat": (1,2), "sunscreen": (3,2), "food": (6,4), "water": (5,3)}
knap_sack(5, items) == 8
```
You could either bring a hat and water on your trip, which would give you a total weight of 5lbs in your knapsack, and a value of 6. Or you could only bring food on your trip, which would give you  total weight of 4lbs in your knapsack and a value of 6.

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory