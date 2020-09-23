# Class Protocols - Vector Class Definition

## Problem Description
Define a python magic method `__eq__` in the `Vector3D` class that checks if two vector objects are equal to each other. Two vectors `vec1` and `vec2` are equal if `x1 = x2` and `y1 = y2` and `z1 = z2`.

For Exmaple:
```
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec3 = Vector3D(1, 5, 3)

vec1 == vec2 == False
vec1 == vec3 == True
```
## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory