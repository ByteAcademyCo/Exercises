# Class Protocols - Vector Class Definition

## Problem Description
Redefine your python magic method `__mul__` as well as the magic methos `__rmul__` in the `Vector3D` to handle both scaler multiplication and vector multipliation. `__rmul__` is the right hand multiplication `other * self`. By defining both `__mul__` and `__rmul__`, this allows you to multiply by a value on either side of the `*` operator.
If we multiply two vectors (take the dot product) for `vec1 = (x1, y1)` and `vec2 = (x2, y2)` the resulting vector will be `x1 * x2 * x3 + y1 * y2 * z2`. If we multiply a vector by an integer `c`, `c * (x1, x2, x3)` or `(x1, x2, x3) * c` the resulting vetor will be `cx1, c2x, cx3`.

For Exmaple:
```
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
vec1 * vec2 == 18

3 * vec1 == Vector3D(3, 15, 9)
vec2 * 2 == Vector3D(8, 8, 2)
```
## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory