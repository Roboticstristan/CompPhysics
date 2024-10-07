from stuff import*

#enviornmentals
g = Vec(0,-9.8,0)
p=1.225
dt = 0.01
t = 0

run = True
#launch parameters

speed = 30
angle = 45

baseball = Projectile(0.145,0.037,Vec(0,0,0),speed,angle)

#weight returns the force of the object
def weight(a):
    return a.m*g

#returns the drag of the object
def drag(a):
    return -0.5 * a.C * a.A * p * abs(a.vel) * a.vel

def move(a):
    global t
    
    force = weight(a)+drag(a)
    acc = force/a.m
    a.vel += acc*dt
    a.pos += a.vel*dt
    t+=dt
    checker(a)
    
def checker(a):
    global run
    if a.pos.y < 0:
        print(a.pos.x)
        run = False
        
    