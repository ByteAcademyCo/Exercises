class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
