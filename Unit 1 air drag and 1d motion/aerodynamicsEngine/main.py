#this is where all the graphics go
import pygame as pg
import sys
import os
from physicsEngine import*

pg.init()
w=800
h=600


screen=pg.display.set_mode((w,h))
pg.display.set_caption("Name")
clock=pg.time.Clock()

while faller.check(): #main loop "game loop"
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                run=False
    move(faller)

    clock.tick(60)
    screen.fill((200,226,250))
    pg.draw.rect(screen,(180,225,180), (0, h-100, w,100))
    pg.draw.circle(screen,(0,0,0), (w/2,100-faller.pos), 5)
    pg.display.flip()

print(faller.vel)
print(t)
pg.quit()
sys.exit()