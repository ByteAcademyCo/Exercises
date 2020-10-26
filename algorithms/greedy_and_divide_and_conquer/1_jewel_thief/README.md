# Greedy Algorithm - Jewel Thief

## Motivation
A greedy algorithm is a type of algorithm that builds up a solution piece by piece always choosing the piece that offers the most imediate benifit. We choose the locally optimal solution at each step to get a globally optimal solution to the problem.


## Problem Description
You are a jewel thief and you are going on a heist at a jewel museum. You bring with you a bag with a maximum capacity of `xkg`. The jewels in the museum are represented as a list of tuples `(weight, value)` where the weight is the weight of the given jewel in kg and the value is the monetary value of the given jewel.
In the *solution.py* file, define a function `steal_jewels` that takes in the maximum capacity of your bag `x` and a list of jewels in the museum `jewels` and outputs the maximal value of jewels you can steal from the museum. If a jewel is too heavy for your bag, you may smash the jewel on the floor and take a fraction of the jewel. 

## Example
```
jewels = [(1, 4), (2, 8), (3, 15), (9, 50)]
steal_jewels(10, jewels) == 55
```
In this example we get the highest value by stealing the last jewel at `9kg` with a value of `50`, and we smash the third jewel and take a third of it at 1kg with a value of `5`, which gives us a full bag at 10kg with a total value of `55`.


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
