#where we make our classes 
import math
class Car :
    def __init__(self,mass, pos, vel,force, dragC):
      self.mass = mass
      self.pos = pos
      self.vel = vel
      self.acc = 0
      self.f = force
      self.A =  1.98
      self.C = dragC
    def __str__(self):
        return str(self.mass)
    def check(self):
      if(self.pos<0):
        return False
      return True
