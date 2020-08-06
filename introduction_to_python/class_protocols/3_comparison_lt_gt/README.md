# Class Protocols - Vector Class Definition

## Problem Description
Define a python magic method `__lt__` in the `Vector3D` class that compares is one vector is less than another vector by magnitude.
Define a python magic method `__gt__` in the `Vector3D` class that compares is one vector is greater than another vector by magnitude. We compute the magnitude of a 3D vector `vect` using the formula `magnitude = sqrt(vect.x**2 + vect.y**2 + vect.z**2)`. In order to use python's buit in sqrt function, you will need to import python's math module and use `math.sqrt()`.

For Exmaple:
```
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec3 = Vector3D(1, 5, 2)

vec1 < vec2 => False
vec1 < vec3 => True
vec1 > vec2 => True
vec1 > vec3 => False
```
## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory