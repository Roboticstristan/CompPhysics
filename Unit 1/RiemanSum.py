import math

time = 0
rate = 0
total = 0


step = 0.00000001

while time <100:
    rate = 0.5*time
    total += rate * step
    time += step
   # print("total made",total,time)
   
print("total made",total,time)
    