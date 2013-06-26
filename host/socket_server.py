#!/usr/bin/env python 

import sys, socket
import pygame
import time

if (len(sys.argv) < 2):
    print "expected port number!"
    print "example: socket_server.py 5001"
    exit(1)

port = int(sys.argv[1])

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def printscreen(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    
pygame.init()

# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create the socket
server_socket.bind(('', port)) # listen on port 5000
server_socket.listen(5) # queue max 5 connections
my_ip = str(socket.gethostbyname(socket.gethostname()))

textPrint.reset()
screen.fill(WHITE)
textPrint.printscreen(screen, "Your IP is {}".format(my_ip))
textPrint.indent()
textPrint.printscreen(screen, "Waiting for client connection on port {} ".format(port) )
textPrint.indent()

pygame.display.flip()
#clock.tick(20)

client_socket, address = server_socket.accept()
print "Your IP address is: ", socket.gethostbyname(socket.gethostname())
print "Server Waiting for client on port ", port

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
    if (joystick_count > 1):
        textPrint.printscreen(screen, "{} joysticks found, using first".format(joystick_count) )
        textPrint.indent()
    elif (joystick_count == 0):
        textPrint.printscreen(screen, " No joysticks found, waiting...")
        textPrint.indent()
        pygame.display.flip()
        clock.tick(20)
        continue
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Get the name from the OS for the controller/joystick
    name = joystick.get_name()
    textPrint.printscreen(screen, "Joystick name: {}".format(name) )
    
    # Usually axis run in pairs, up/down for one, and left/right for
    # the other.
    axes = joystick.get_numaxes()
    textPrint.printscreen(screen, "Number of axes: {}".format(axes) )
    textPrint.indent()
    data = [] 
    for i in range( axes ):
        axis = joystick.get_axis( i )
        data.append("%02d," % (float(`axis`)*100))
        textPrint.printscreen(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
    textPrint.unindent()
        
    buttons = joystick.get_numbuttons()
    textPrint.printscreen(screen, "Number of buttons: {}".format(buttons) )
    textPrint.indent()

    for i in range( buttons ):
        button = joystick.get_button( i )
        textPrint.printscreen(screen, "Button {:>2} value: {}".format(i,button) )
    textPrint.unindent()
        
    # Hat switch. All or nothing for direction, not like joysticks.
    # Value comes back in an array.
    hats = joystick.get_numhats()
    textPrint.printscreen(screen, "Number of hats: {}".format(hats) )
    textPrint.indent()

    for i in range( hats ):
        hat = joystick.get_hat( i )
        textPrint.printscreen(screen, "Hat {} value: {}".format(i, str(hat)) )
    textPrint.unindent()
    
    textPrint.unindent()
   
    # send the x and y axis value to socket server
    client_socket.sendall(''.join(data))
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)

client_socket.sendall("999,999")
socket.close()
p.terminate()
pygame.quit ()
