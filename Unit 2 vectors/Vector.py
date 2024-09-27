import math
class Vector:
    
    def __init__(self,x,y,z):
        self.x = (float) (x)
        self.y = (float) (y)
        self.z = (float) (z)
        
    def __add__(self,v):
        if isinstance(v, Vector):
            return Vector(self.x + v.x, self.y + v.y, self.z + v.z)
        raise TypeError(f"Cannot add vector with {type(v)}")
    
    def __sub__(self,v):
        if isinstance(v, Vector):
            return Vector(self.x + -1*v.x, self.y + -1*v.y, self.z + -1*v.z)
        raise TypeError(f"Cannot subtract vector with {type(v)}")
    
    def __mul__(self,v):
        if not isinstance(v, (float,int)):
            raise TypeError(f"Cannot multiply vector with {type(v)}, your type is not a scalar")
        return Vector(self.x * v, self.y * v, self.z * v)
    
    def __truediv__(self,v):
        if not isinstance(v, (float,int)):
            raise TypeError(f"Cannot multiply vector with {type(v)}, your type is not a scalar")
        return Vector(self.x / v, self.y / v, self.z / v)
    
    def findMag(self):
        return(math.sqrt(self.x**2 + self.y**2 + self.z**2))
    
    def Normalize
    
    def __str__(self):
        return str(self.x) + " "+ str(self.y)+ " " + str(self.z)
    
Vecc = Vector(2,3,5)
vic = Vector(1,3,7)

print(Vecc*1)
