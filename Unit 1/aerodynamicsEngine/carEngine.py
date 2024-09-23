#where all the math gets done
import car
import math
t = 0
dt = 0.01
p= 1.15

faller= car.Car(1435,0,0,13000,0.33)
run = True

def move(a):
    global run
    global t

    #improved stuff from website
    drag = 1/2 * a.C * a.A * p * a.vel**2
    #calculated net forces
    force=(a.f)-(drag)
    #self explanatory dont be special on the code walk
    a.acc=(force)/a.mass
    a.pos+=a.vel*dt
    a.vel+=a.acc*dt
    t += dt
    #happens once parachute is deployed
    if((a.vel*60*60*100)/(2.54*12*5280) >= 124):
        run = False 
        print(t)
        #changes the are and drag coefficent
        # a.A = 3**2 * math.pi
        # a.C = 1.6
    #used if need to calculate total time
    # if(a.pos <= 0):
    #     run = False 
    #     print(t)
    #     print(a.vel)

while run:
     move(faller)