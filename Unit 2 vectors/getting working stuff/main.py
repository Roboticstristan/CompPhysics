import projectileEngine as pe
import graphics as gx

gx.setup(800,600)
gx.background()

while pe.run==True:
    gx.check_interactions() 
    gx.frameRate(60)
    gx.render(pe.baseball)
    pe.move(pe.baseball, 30)

gx.pg.quit()
#this import only imports the run boolean once and wont pick up any changes to it
# from projectileEngine import*

# while run:
#     move(baseball) 