# Class Protocols - Vector Class Definition

## Problem Description
Define a python magic method `__mul__` in the `Vector3D` class that computes the dot product of two vector objects. If we multiply two vectors (take the dot product) for `vec1 = (x1, y1)` and `vec2 = (x2, y2)` the resulting vector will be `x1 * x2 * x3 + y1 * y2 * z2`.

For Exmaple:
```
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec1 * vec2 == 18
```
## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory