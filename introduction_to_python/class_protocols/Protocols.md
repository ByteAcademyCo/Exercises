# Protocols

* Create a class called Vector3D that is initalized with 3 integers - x, y, z
* The Vector3D class should support the following operations. For each operation, there is sample code that should pass
  * Initialization
  * Printing
  * Airthmetic (Additon, Subtraction, Multiplication, Comparison)
  * Iteration

* Initialization
```Python
vec1 = Vector3D(1,2,3)
vec2 = Vector3D(9,8,7)
vec1.x == 1
vec1.y == 2
vec1.z == 3
```

* Printing
```Python
print(vec1) == '(x = 1, y = 2, z = 3)'
print(vec2) == '(x = 9, y = 8, z = 7)'
```

* Addition, Subtraction
```Python
(vec1 + vec2).x == (vec1 + vec2).y == (vec1 + vec2).z
vec3 = vec1 - vec2
vec3.x == -8
vec3.y == -6
vec3.z == -4
```

* Multiplication ([Dot Product](https://en.wikipedia.org/wiki/Dot_product))
```Python
vec1 * vec2 == 46 # (1*9 + 2*7 + 3*7 = 46)
```

* Comparison ([Magnitude](https://en.wikipedia.org/wiki/Magnitude_(mathematics)#Euclidean_vector_space))
```Python
vec1 < vec2 == True
```

* Iteration - output x, y, z coordinates in that order
```Python
vec_diff = 0
for i in vec1:
  vec_diff -= i
vec_diff == -4
```
