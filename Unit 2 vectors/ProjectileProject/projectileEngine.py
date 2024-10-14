from stuff import*


#enviornmentals
g = Vec(0,-9.8,0)
p=1.2
dt = 0.001
t = 0

maxHeight = 0

run = True
go = False
#launch parameters

lHeight = float(input())

lSpeed = float(input())

lAngDeg = float(input())

# lHeight = 12.5

# lSpeed = 12.3

# lAngDeg = 35.0

speed = lSpeed
angle = lAngDeg

baseball = Projectile(42,0.18,Vec(0,lHeight,0),speed,angle)

#weight returns the force of the object
def weight(a):
    return a.m*g

#returns the drag of the object
def drag(a):
    return -0.5 * a.C * a.A * p * abs(a.vel) * a.vel

def netForce(a):
    return weight(a)+drag(a)

def move(a,reps):
    global t
    if go == True:
     for i in range(reps):
        t += dt
        force = weight(a)+drag(a)
        acc = force/a.m
        a.vel += acc*dt
        a.pos += a.vel*dt
        checker(a)

    
def checker(a):
    global run
    if(abs(a.vel.y)<0.01):
        print(f'max height = {round(a.pos.y,2)} m')

    if(a.pos.y<0):
        print(f'range = {round(a.pos.x,2)}')
        print(f'Final speed = {round(a.vel.mag(),2)} m/s')
        print(f'Total time of flight = {round(t,2)} s')
        run = False

        
    