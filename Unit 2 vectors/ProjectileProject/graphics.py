#render
import pygame as pg
scale=10

def setup(w,h):
    global screen
    global clock
    pg.init()
    screen=pg.display.set_mode((w,h))
    pg.display.set_caption("Projectiles")
    clock=pg.time.Clock()
def background():
    screen.fill((200, 225, 250))
    pg.draw.rect(screen, (180, 255, 180), (0, 500, 800, 100))
def render(a):
    background()
    pg.draw.circle(screen,(0,0,0),(scale*a.pos.x,500-1*scale*a.pos.y),5)
    pg.display.flip()
    clock.tick(60)
