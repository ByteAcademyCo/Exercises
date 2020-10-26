# Greedy Algorithm - European Coin Change

## Motivation
A greedy algorithm is a type of algorithm that builds up a solution piece by piece always choosing the piece that offers the most imediate benifit. We choose the locally optimal solution at each step to get a globally optimal solution to the problem.


## Problem Description
In the *solution.py* file, define a function `make_change` that consumes a positive integer `amount` which will be a monertary value given in Euro cents, and a list of coin values `denominations` given in european cent denominations, and using a greedy algorithm, returns the minimum number of coins needed to make change for `amount`. If you cannot make change for `amount` return `-1`. 

## Example
```
denominations = [1, 2, 5, 10, 20, 50, 100, 200]
make_change(450, denominations) == 3
```
In this example we use two 200c (2€) coins and one 50c coin.


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
