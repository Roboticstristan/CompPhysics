#where all the math gets done
import ball

t = 0
dt = 0.1
g = 9.8
mass = 10

ball = ball.Ball(mass,0.1,10,0, -1*g*mass, 0.5)

def move(a):
    global dt
    a.acc =a.force/a.mass
    a.vel+=a.acc*dt
    a.pos+=a.vel*dt
    if a.pos < 0:
       print(a.vel)
       a.vel = 0
       a.dt = 0
       