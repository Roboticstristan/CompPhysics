#where we make our classes 
import math
class Ball:
    def __init__(self,mass, rad, pos, vel, force, dragC):
      self.mass = mass
      self.pos = pos
      self.vel = vel
      self.acc = force/mass
      self.force = force
      self.A = rad**2 * math.pi 
      self.C = dragC
    def __str__(self):
        return str(self.mass)
