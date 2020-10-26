# Greedy Algorithm - Frog Hops

## Motivation
A greedy algorithm is a type of algorithm that builds up a solution piece by piece always choosing the piece that offers the most imediate benifit. We choose the locally optimal solution at each step to get a globally optimal solution to the problem.

## Problem Description
Kermit the frog is standing on a lily pad at position `0` on the river. Kermit wants to get to get to the lily pad at position `n` on the river. We will represent the river as an array `river` where `river[i] = 1` if there exists a lily pad at position `i` and `river[i] = 0` if there is no lily pad at position `i` on the river. Kermit can hop up to `x` units at a time along the river.
In the *solution.py* file, define a function `min_hops` that takes in the maximum number of units `max_units` Kermit can move in one hop, and `n` the position on the river Kermit is trying to reach, and `river`, the array representation of the river with lily pads, and outputs the minimum number of hops Kermit can make to get to position `n`. Output `-1` if it is impossible for Kermit to reach the lily pad at position `n`. 

## Example
```
river = [1, 0, 0, 1, 1, 0, 0, 1]
min_hops(3, 7, river) == 3
```
In this example Kermit can first make one hop to jump 3 spaces to the lily pad at position `3`. He then he makes another hop to move one space to get to the lily pad at position `4`, and he makes a final hop to move 3 spaces to get to the lily pad at position `7`.


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
