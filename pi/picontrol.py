#!/usr/bin/env python 
import pygame
from pygame.locals import *
import pygame.gfxdraw

width = 480/4
height = 480/4

red      = ( 255,   0,   0)
white    = ( 255, 255, 255)
black    = ( 0, 0, 0)

def draw_arrow(screen,x,y, color, direction):
    # draw the line
    if (direction < 2):
        pygame.draw.line(screen,color,[x,y-9],[x,y+9],6)
    else:
        pygame.draw.line(screen,color,[x-9,y],[x+9,y],6)
    # draw arrow head
    if (direction == 0):
        pygame.gfxdraw.filled_trigon(screen, x, y-14, x-10, y-4, x+10, y-4, color)
    elif (direction == 1):
        pygame.gfxdraw.filled_trigon(screen, x, y+14, x-10, y+4, x+10, y+4, color)
    elif (direction == 2):
        pygame.gfxdraw.filled_trigon(screen, x+14, y, x+4, y+10, x+4, y-10, color)
    elif (direction == 3):
        pygame.gfxdraw.filled_trigon(screen, x-14, y, x-4, y+10, x-4, y-10, color)


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('bot control')

pygame.mouse.set_visible(1)
screen.fill(white)
# draw dot in the middle
pygame.draw.ellipse(screen,red,[width/2-10,height/2-10,22,22],0)

clock=pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            done = True
        if (event.type == KEYUP) or (event.type == KEYDOWN):
            print event
            if (event.key == K_ESCAPE):
                done = True
            if (event.type == KEYDOWN):
                if (event.key == K_UP):
                    draw_arrow(screen, width/2,height/2-20, black,0 )
                elif (event.key == K_DOWN):
                    draw_arrow(screen, width/2,height/2+20, black,1 )
                elif (event.key == K_RIGHT):
                    draw_arrow(screen, width/2+20,height/2, black, 2)
                elif (event.key == K_LEFT):
                    draw_arrow(screen, width/2-20,height/2, black, 3)
            if (event.type == KEYUP):
                if (event.key == K_UP):
                    draw_arrow(screen, width/2,height/2-20, white, 0)
                elif (event.key == K_DOWN):
                    draw_arrow(screen, width/2,height/2+20, white, 1)
                elif (event.key == K_RIGHT):
                    draw_arrow(screen, width/2+20,height/2, white, 2)
                elif (event.key == K_LEFT):
                    draw_arrow(screen, width/2-20,height/2, white, 3)
        pygame.display.flip()
        clock.tick(25)

