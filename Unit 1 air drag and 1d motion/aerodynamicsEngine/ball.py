#where we make our classes 
import math
class Ball:
    def __init__(self,mass, rad, pos, vel, dragC):
      self.mass = mass
      self.pos = pos
      self.vel = vel
      self.acc = 0
      self.A =  0.45
      self.C = dragC
    def __str__(self):
        return str(self.mass)
    def check(self):
      if(self.pos<0):
        return False
      return True
