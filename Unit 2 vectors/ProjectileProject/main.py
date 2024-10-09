import projectileEngine as pe

while pe.run==True:
    pe.move(pe.baseball)

#this import only imports the run boolean once and wont pick up any changes to it
# from projectileEngine import*

# while run:
#     move(baseball)