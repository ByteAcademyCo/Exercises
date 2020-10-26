# Greedy Algorithm - Scheduling Tasks

## Motivation
A greedy algorithm is a type of algorithm that builds up a solution piece by piece always choosing the piece that offers the most imediate benifit. We choose the locally optimal solution at each step to get a globally optimal solution to the problem.

## Problem Description
Your boss gives you a list of tasks you have to complete on that day for your job, each with a start time and end time given as a tuple `(start, end)`. `Start` and `end` will be given in hrs on a 24hr clock. 
In the *solution.py* file, define a function `task_schedule` that takes in the list of tasks `tasks`, and outputs the maximum number of tasks you can complete in the day. You cannot do more than one task at a time. Hint: Sort the list by finishing time.

## Example
```
tasks = [(14, 15), (8, 13), (9, 11), (11, 13), (14, 16)]
task_schedule(tasks) == 3
```
In this example, we can do the task from 9am-11am, the next task from 11am-1pm, and the final task from 2pm-4pm.

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
