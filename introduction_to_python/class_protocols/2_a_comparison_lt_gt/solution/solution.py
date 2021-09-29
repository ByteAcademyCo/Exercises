import math


class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __it__(self, other):
        if self.x < other.x:
            return math.sqrt(x)
        elif self.y < other.y:
            return True
        else:
            self.z < other.z
            return True

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.y > other.y:
            return True
        else:
            self.z > other.z
            return True


print(vec1=math.sqrt((1, 5, 3)))
print(vec2=math.sqrt((4, 4, 1)))
print(vec3=math.sqrt((1, 5, 2)))
