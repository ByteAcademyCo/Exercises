# Towers Of Hanoi

## Motivation
Towers of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack from one rod to another, obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.

For a further explanation on this concept, please consult the [wikipedia](https://en.wikiepdia.org/wiki/Tower_of_Hanoi) page.

## Problem Description
Define a recursive Python function named `tower_of_hanoi`. The function consumes 4 arguments:
* `n` - the number of disks
* `from_rod` - the starting rod with all the disks (a list of integers representing the size of the disk)
* `to_rod` - the desintation rod to end with all the disks
* `aux_rod` - an auxiliary rod to assist with moving the disks

The function returns the minimal number of moves required to get all the disks from `from_rod` to `to_rod`.

## Examples
```
tower_of_hanoi(2, [2, 1], [], []) == 3
tower_of_hanoi(3, [3, 2, 1], [], []) == 7
```
## Testing
* To test your solution, type 'pytest' within the solution subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solutions* subdirectory within this directory
