class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return (
            "(x = "
            + str(self.x)
            + ", y = "
            + str(self.y)
            + ", z = "
            + str(self.z)
            + ")"
        )

    def __mul__(self, other):
        if type(other) == int:
            return Vector3D(self.x * other, self.y * other, self.z * other)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, other):
        if type(other) == int:
            return Vector3D(self.x * other, self.y * other, self.z * other)
        return self.x * other.x + self.y * other.y + self.z * other.z

vec1 = Vector3D(1, 2, 3)
print(3 * vec1)
