import pygame
import sys
# pygame setup
pygame.init()
 

screenW = 1000
screenH = 800

canvas = pygame.display.set_mode((screenW,screenH))
canvas.fill((100,150,255))

velo = 0
acc = 9.8
t = 0
posY = 10
dt = 0.001 #step

canvas.fill((100,150,255))
sun = pygame.draw.circle(canvas,(255,225,0),(screenH*0.5,screenW*0.5),10,10)
x = pygame.draw.rect(canvas,(20,200,20),(0,0.8 * screenH,screenW,0.2 * screenH))
pygame.display.flip()

run = True
while run:
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
                run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                while sun.centerx < screenH -sun.width/2:
                    velo +=acc * dt
                    posY += velo * dt
                    t+=dt
                    canvas.fill((100,150,255))
                    x = pygame.draw.rect(canvas,(20,200,20),(0,0.8 * screenH,screenW,0.2 * screenH))
                    sun = pygame.draw.circle(canvas, (255,225,0), (screenW*0.5, posY), 10)
                    pygame.display.flip()
                run = False


print(posY,t)          
pygame.quit()
exit()