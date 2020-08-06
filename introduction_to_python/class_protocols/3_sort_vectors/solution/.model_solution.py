import math
class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return '(x = '+ str(self.x) + ', y = '+ str(self.y) + ', z = '+ str(self.z) + ')'

    def magnitude(self):
            return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()
    
    def __eq__(self, other):
        return (self.x == other.x and 
                self.y == other.y and 
                self.z == other.z)
    

def sort_vectors(vect_lst):
    return sorted(vect_lst)
