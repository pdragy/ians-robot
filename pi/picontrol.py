#!/usr/bin/env python 
import pygame
import time
import RPi.GPIO as GPIO
from pygame.locals import *
import pygame.gfxdraw

GPIO.setmode(GPIO.BOARD)
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

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.output(3,1) 
GPIO.output(5, 1)
GPIO.output(7, 1)
time.sleep(0.5)
p = GPIO.PWM(11, 50)  # channel=12 frequency=50Hz
s = GPIO.PWM(13, 50)  # channel=12 frequency=50Hz
l = GPIO.PWM(8, 50)  # channel=12 frequency=50Hz
r = GPIO.PWM(10, 50)  # channel=12 frequency=50Hz

l.start(0)
r.start(0)
p.start(0)
s.start(0)


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
		    p.ChangeDutyCycle(0)
		    s.ChangeDutyCycle(75)
                    draw_arrow(screen, width/2,height/2-20, black,0 )
                elif (event.key == K_DOWN):
		    p.ChangeDutyCycle(75)
		    s.ChangeDutyCycle(0)
                    draw_arrow(screen, width/2,height/2+20, black,1 )
                elif (event.key == K_RIGHT):
		    l.ChangeDutyCycle(100)
		    r.ChangeDutyCycle(0)
                    draw_arrow(screen, width/2+20,height/2, black, 2)
                elif (event.key == K_LEFT):
		    l.ChangeDutyCycle(0)
		    r.ChangeDutyCycle(100)
                    draw_arrow(screen, width/2-20,height/2, black, 3)
            if (event.type == KEYUP):
                if (event.key == K_UP):
		    p.ChangeDutyCycle(0)
		    s.ChangeDutyCycle(0)
                    draw_arrow(screen, width/2,height/2-20, white, 0)
                elif (event.key == K_DOWN):
		    p.ChangeDutyCycle(0)
		    s.ChangeDutyCycle(0)
                    draw_arrow(screen, width/2,height/2+20, white, 1)
                elif (event.key == K_RIGHT):
		    l.ChangeDutyCycle(0)
		    r.ChangeDutyCycle(0)
                    draw_arrow(screen, width/2+20,height/2, white, 2)
                elif (event.key == K_LEFT):
		    l.ChangeDutyCycle(0)
		    r.ChangeDutyCycle(0)
                    draw_arrow(screen, width/2-20,height/2, white, 3)
        pygame.display.flip()
        clock.tick(25)

l.stop()
r.stop()
p.stop()
s.stop()
GPIO.cleanup()
