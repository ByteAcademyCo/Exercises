# Sort Vectors - Sort Vectors by Magnitude

## Motivation
Sorting is one of the most studied type of algorithms in computer science. There are many different sorting algorithms which may have different benifits and drawbacks given the problem you are trying to solve and your data. You must consider your time contraints and space constraints when choosing the appropriate sorting algorithm for your problem.
Sorting is important because it allows us to optimize data searching to a very high level, when data is stored in a sorted manner. Sorting also allows us to represent data in more readable formats.

## Problem Description
In the *solution.py* file, define a function `sort_vectors` that consumes a lists of vecotrs `vector_lst`, which is a list of tuples of tuples `((x1, y1), (x2, y2))` coordinates, and sorts the list of vectors in increasing order by magnitude. Hint: The magnitude of a vector can be calculated using the formula `magnitude = sqrt((x2 - x1)**2 + (y2 - y1)**2)`.

## Example
```
vector_lst = [((1, 3), (2, 6)), ((1, 5), (3, 4)), ((2, 6), (2, 9))]
sort_vectors(vector_lst) == [((1, 5), (3, 4)), ((2, 6), (2, 9)), ((1, 3), (2, 6))]
```
The magnitude of the first vector in `vector_lst` is sqrt(10), the magnitude of the second vector is sqrt(5), and the magnitude of the third vector is sqrt(9). Thus we sort the list accordingly.

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
