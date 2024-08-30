#imports the pygame library
import pygame
import sys
# pygame setup
pygame.init()
 
#
screenW = 1000
screenH = 800

#creates the display window object with the given width and heights
canvas = pygame.display.set_mode((screenW,screenH))
canvas.fill((100,150,255))
posx = 0
posy = 0
x = pygame.draw.rect(canvas,(20,200,20),(0,0.8 * screenH,screenW,0.2 * screenH))
sun = pygame.draw.circle(canvas,(255,225,0),(screenH*0.2 -50,screenW*0.15),50,50)
pygame.draw.ellipse(canvas,(255,255,255), (screenW * 0.35,0.15 * screenH, screenW * 0.55, 0.15 * screenH))
pygame.display.flip()

run = True
while run:
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE :
                while sun.centerx != screenW - sun.width/2:
                    rate = 2
                    canvas.fill((100,150,255))
                    posx = sun.centerx + rate
                    posy = sun.centery
                    pygame.draw.ellipse(canvas,(255,255,255), (screenW * 0.35,0.15 * screenH, screenW * 0.55, 0.15 * screenH))
                    x = pygame.draw.rect(canvas,(20,200,20),(0,0.8 * screenH,screenW,0.2 * screenH))
                    sun = pygame.draw.circle(canvas, (255,225,0), (posx, posy), 50)
                    pygame.display.flip()
                    
            
pygame.quit()
exit()
