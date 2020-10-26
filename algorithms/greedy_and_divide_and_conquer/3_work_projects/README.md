# Greedy Algorithm - Work Projects

## Motivation
A greedy algorithm is a type of algorithm that builds up a solution piece by piece always choosing the piece that offers the most imediate benifit. We choose the locally optimal solution at each step to get a globally optimal solution to the problem.

## Problem Description
Your boss gives you a list of work projects each with a deadline and profit given as a tuple `(deadline, profit)`. The deadline will be an integer representing the time unit after which the project cannot be executed. Each project takes one unit of time. For example, a project with a deadline of `2` can only be executed in the first or second time slot. Profit will be an integer represeting the total profits earned from completing that project.
In the *solution.py* file, define a function `max_profits` that takes in the list of projects `projects`, and outputs the maximal profits you can make given the list of projects. Hint: Sort the list by maximal profit.

## Example
```
projects = [(1, 100), (2, 150), (2, 300), (4, 200), (3, 100)]
max_profits(projects) == 750
```
In this example, we choose to execute `(2, 150)` in the first time slot, we execute `(2, 300)` in the second time slot, we execute `(3, 100)` in the third time slot, and we execute `(4, 200)` in the fourth time slot.

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
