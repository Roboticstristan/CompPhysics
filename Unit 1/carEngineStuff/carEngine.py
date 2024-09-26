
#where all the math gets done
import car
import math
t = 0
dt = 0.01
p= 1.15

speedster= car.Car(1435,0,0,13000,0.33)
run = True

def move(a):
    global run
    global t

    #improved force calculation
    a.f = 15400 - 128* a.vel
    #drag calculation   
    # tailwind = 57.78042
    # airspeed = a.vel - tailwind
    airspeed = a.vel
    drag = 1/2 * a.C * a.A * p * airspeed* abs(airspeed)
    #calculated net forces
    force=(a.f)-(drag)
    #self explanatory dont be special on the code walk
    a.acc=(force)/a.mass
    a.pos+=a.vel*dt
    a.vel+=a.acc*dt
    t += dt
    print(a.f,drag)
    
    #goes off once the condition is met in this case once the mile is hit
    # if((a.pos*100)/(2.54*12*5280) >= 1):
    #     run = False 
    #     print(t)
    
    #used to calculate max speed
    if(a.f <= drag+0.0000001):
        run = False 
        print((a.vel*60*60*100)/(2.54*12*5280))
    
    #used to find when a speed has been met (converts the velocity to mph)  
    # if((a.vel*60*60*100)/(2.54*12*5280) >= 124):
    #     run = False 
    #     print(t)
 
 
while run:
     move(speedster)
