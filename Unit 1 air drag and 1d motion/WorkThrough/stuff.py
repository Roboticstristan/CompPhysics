#where we make our classes 
class Car:
    def __init__(self,mass,pos,vel, acc, force):
      self.mass = mass
      self.pos = pos
      self.vel = vel
      self.acc = acc
      self.force = force
    def __str__(self):
        return str(self.mass)
