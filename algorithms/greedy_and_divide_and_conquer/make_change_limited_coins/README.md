# Greedy Algorithm - European Coin Change with Limited Coins

## Motivation
A greedy algorithm is a type of algorithm that builds up a solution piece by piece always choosing the piece that offers the most imediate benifit. We choose the locally optimal solution at each step to get a globally optimal solution to the problem.

## Problem Description
In the *solution.py* file, define a function `make_change` that consumes a positive integer `amount` which will be a monertary value given in Euro cents, and a list `denominations` which is a dictionary of `{value: count}` where value is the value of a coin, given in european cent denominations, and `count` is how many of that coin you have in your pocket. Using a greedy algorithm, return the minimum number of coins needed to make change for `amount`, given the coins in your pocket. If you cannot make change for `amount` return `-1`. 

## Example
```
denominations = {1: 5, 2: 1, 10: 5, 50: 3, 100: 1, 200: 1}
make_change(450, denominations) == 5
```
In this example we use one 200c (2€) coin, one 100c (1€) coin, and all three of our 50c coins.


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
