# Class Protocols - Vector Class Definition

## Problem Description
Define a python magic method `__mul__` in the `Vector3D` class that computes the dot product of two vector objects. If we multiply two vectors (take the dot product) for `vec1` and `vec2` the resulting vector will be `vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z`.

For Exmaple:
```
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec1 * vec2 => 18
```
## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory