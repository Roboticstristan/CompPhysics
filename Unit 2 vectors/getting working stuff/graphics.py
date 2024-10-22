#render

import pygame as pg
import projectileEngine as phys


ballS= 10
screenSH = 1
screenSW = 1
ogPos =[]
height = 0
width = 0

def setup(w,h):
    global height
    global width
    height = h
    width = w
    global screen
    global clock
    pg.init()
    screen=pg.display.set_mode((w*screenSW,h*screenSH))
    # screen=pg.display.set_mode((w,h))

    pg.display.set_caption("Projectiles")
    clock=pg.time.Clock()

def background():
    screen.fill((200, 225, 250))
    pg.draw.rect(screen, (166, 139, 113), (0,screen.get_height()-50,screen.get_width(),50))
    # pg.draw.rect(screen, (180, 255, 180), (0, 800, 800,100))

#draws all the circles based on cordinates ive stored in the list A is meant to be a list filed w tuples
# and then multiplies them by the ball scale to draw them in a for loop also adds a ground
def drawCircles(a):
    for (X,Y) in a:
        pg.draw.circle(screen,(11, 218, 81),(X*ballS, screen.get_height()-50+Y*ballS),5)
    pg.draw.rect(screen, (166, 139, 113), (0,screen.get_height()-50,screen.get_width(),50))

def checker():
    #autoscaling graphics done by this puppy essentially checks the last thing in the positions list
    #if that spot after being scaled is to close the the edge of the screen ball scale is reduced essentially making it so that
    #the ball will fit inside of the screen by reducing scale as ball approaches side
    global screenSW
    global screenSH
    global screen
    global ballS
    #position is stored in ogPos list which stores tuples containing x and y coordinates
    positionTuple = ogPos[len(ogPos)-1]
    x = positionTuple[0] * ballS
    y = positionTuple[1] * ballS 
    #checks if the ball is to close to the screen
    if(screen.get_width() - x < 5):
        ballS -= 0.125
        # screenSW += 0.01
        # screen=pg.display.set_mode((width*screenSW,height*screenSH))
    

    
def render(a):
    global ogPos
    background()
    ogPos.append((a.pos.x,-1*a.pos.y))
    checker()
    drawCircles(ogPos)
    pg.display.flip()

   
def frameRate(a):
    clock.tick(a)

def check_interactions():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            phys.run=False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                phys.go = True       

    