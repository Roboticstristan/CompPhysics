#where all the math gets done
import ball
import math
t = 0
dt = 0.01
g = 9.8

mass = 70

faller= ball.Ball(70,0.1,3700,0,1.4)
run = True

def move(a):
    global run
    global t
    temp = 15.04 - (0.00649 * a.pos) 
    pressure = (((temp + 273.1)/288.08)**5.256)
    drag=-0.5*a.C*a.A*pressure*a.vel*abs(a.vel)
    force=(-a.mass*g)+(drag)
    a.acc=(force)/a.mass
    a.pos+=a.vel*dt
    a.vel+=a.acc*dt
    t += dt
    if(a.pos <= 1000):
        run = False 
        print(t)
        print(a.vel)
        # a.A = 3**2 * math.pi
        # a.C = 1.6
    # if(a.pos <= 0):
    #     run = False 
    #     print(t)
    #     print(a.vel)

while run:
     move(faller)