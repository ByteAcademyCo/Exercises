# Class Protocols - Vector Class Definition

## Problem Description
Define a python magic method `__sub__` in the `Vector3D` class that subtracts two vector objects. If we subtract two vectors `vec1 = (x1, y1, z1)` and `vec2 = (x2, y2, z2)` the resulting vector will be `(x1 - x2, y1 - y2, z1 - z2)`.

For Exmaple:
```
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec1 - vec2 == Vector3D(-3, 1, 2)
```
## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory