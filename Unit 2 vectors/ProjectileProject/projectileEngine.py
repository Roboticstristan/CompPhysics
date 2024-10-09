from stuff import*


#enviornmentals
g = Vec(0,-9.8,0)
p=1.2
dt = 0.001
t = 0

maxHeight = 0

run = True
#launch parameters

lHeight = float(input())

lSpeed = float(input())

lAngDeg = float(input())


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

def move(a):
    global maxHeight
    global t
    force = weight(a)+drag(a)
    acc = force/a.m
    a.vel += acc*dt
    a.pos += a.vel*dt
    t+=dt
    if(a.pos.y > maxHeight):
        maxHeight = a.pos.y
    checker(a)

    
def checker(a):
    global run
    if a.pos.y < 0:
        print(t)
        print(a.pos.x)
        print(a.vel.mag())
        print(maxHeight)
        run = False
        
    