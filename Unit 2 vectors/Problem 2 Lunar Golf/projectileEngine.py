from golfBall import*


#enviornmentals
g = Vec(0,-9.8,0)
airDen = 1.2    
dt = 0.001
t = 0

maxHeight = 0

run = True
go = False
#launch parameters

speed = 60

angleDeg = 20.0

lHeight = 0

launchSpin = 40

DragC = 0.5

MagC = 0.004

wind = Vec(12,0,0)

angularVel = Vec(0,0,launchSpin)

baseball = Projectile(0.5,0.08,Vec(0,lHeight,0),speed,angleDeg,DragC,MagC)

#weight returns the force of the object
def weight(a):
    return a.m*g


def voa(a):
    return a.vel - wind
#returns the drag of the object
def drag(a):
    return -0.5 * a.C * a.A * airDen * abs(voa(a)) * voa(a)

def magnus(a):
    return a.MC * (angularVel.cross(voa(a)))
    
def netForce(a):
    return weight(a)+drag(a)+magnus(a)

def move(a,reps):
    global t
    if go == True:
     for i in range(reps):
        if(go == False):
            break
        t += dt
        force = netForce(a)
        acc = force/a.m
        a.vel += acc*dt
        a.pos += a.vel*dt
        checker(a)
    
def checker(a):
    global run
    global go
    global maxHeight
    if(abs(a.vel.y)<0.01 and a.pos.y > maxHeight):
        print(f'max height = {round(a.pos.y,2)} m')


    if(a.pos.y<0):
        print(f'range = {round(a.pos.x,2)}')
        print(f'Final speed = {round(a.vel.mag(),2)} m/s')
        print(f'Total time of flight = {round(t,2)} s')
        run = False
        go = False
    
    
    