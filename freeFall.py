rad = 0.25
pos1 = float(input()) + rad
velo1 = float(input())
pos2 = float(input()) - rad
velo2 = float(input())
rad = 0.25
t = 0
dt = 0.0000001 #step
acc = -9.8

run = True
while run:
    velo1 +=acc * dt
    velo2 +=acc * dt
    pos2 += velo2 * dt
    pos1 += velo1 * dt
    t+=dt
    if(pos1 >= pos2 ):
        break
    
print(t, velo1, velo2)          
