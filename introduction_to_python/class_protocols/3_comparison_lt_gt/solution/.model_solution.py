import math
class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
            return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()
