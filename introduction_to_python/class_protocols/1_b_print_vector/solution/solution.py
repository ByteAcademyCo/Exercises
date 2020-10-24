class Vector3D:
    
    def __init__(self, x = 0, y= 0, z= 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f'(x = {self.x}, y = {self.y}, z = {self.z})'
#print(Vector3D(3, 4, 2))