#where all the math gets done
import stuff

bob = stuff.Car(1000,0,0,0,800)

t = 0
dt = 0.1
def move(a):
    a.acc =a.force/a.mass
    a.vel+=a.acc*dt
    a.pos+=a.vel*dt
