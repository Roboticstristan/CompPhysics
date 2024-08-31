x = 0
total = 0
hours = 0
while hours < 100:
    total += x
    hours += 1
    print(total,hours)
    x = 0.5*hours
print(total,hours)