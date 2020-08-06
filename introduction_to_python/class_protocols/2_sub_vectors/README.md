# Class Protocols - Vector Class Definition

## Problem Description
Define a python magic method `__sub__` in the `Vector3D` class that subtracts two vector objects. If we subtract two vectors `vec1` and `vec2` the resulting vector will be `(vec1.x - vec2.x, vec1.y - vec2.y, vec1.z - vec2.z)`.

For Exmaple:
```
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec1 - vec2 = Vector3D(-3, 1, 2)
```
## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory