import math
from vectors import*

class Projectile:
    
    def __init__(self,mass,radius,initial_pos,speed,angle_deg,Dragcoefficent,MagCoefficent):
        self.m = mass
        self.rad = radius
        self.A = math.pi*radius**2
        self.pos = initial_pos
        self.C = Dragcoefficent
        self.MC = MagCoefficent
        self.angRad = math.radians(angle_deg)
        #this sets up the velocity as a vector
        self.vel = Vec((speed*math.cos(self.angRad)),speed*math.sin(self.angRad),0)
