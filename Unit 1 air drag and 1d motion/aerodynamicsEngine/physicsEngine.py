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
    #improved stuff from website
    temp = 15.04 - (0.00649 * a.pos) 
    #took out the *101.somenumber because it was in KPA and i needed it in kg/m^3
    pressure = (((temp + 273.1)/288.08)**5.256)
    #calculates drag
    drag=-0.5*a.C*a.A*pressure*a.vel*abs(a.vel)
    #calculated net forces
    force=(-a.mass*g)+(drag)
    #self explanatory dont be special on the code walk
    a.acc=(force)/a.mass
    a.pos+=a.vel*dt
    a.vel+=a.acc*dt
    t += dt
    # #happens once parachute is deployed
    if(a.pos <= 1000):
        a.A = 3**2 * math.pi
        a.C = 1.6
        # run = False 
        # print(t)
        # print(a.vel)
        #changes the are and drag coefficent
        # a.A = 3**2 * math.pi
        # a.C = 1.6
    #used if need to calculate total time
    if(a.pos <= 0):
        run = False 
        print(t)
        print(a.vel)

while run:
     move(faller)