#!/usr/bin/env python 

import sys, socket
import time
import RPi.GPIO as GPIO

if (len(sys.argv) < 3):
    print "expected server ip address and port number"
    print "example: socket_client.py 192.168.1.118 5001"
    exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])

#port = 5001
#ip = "192.168.1.118"

GPIO.setmode(GPIO.BOARD)

# Do we need these or did we make these always on?
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.output(3,1) 
GPIO.output(5, 1)
GPIO.output(7, 1)

# set up the PWM pins for left/right forward/back control
GPIO.setup(8,  GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# PWM for camera pan/tilt
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

p_back  = GPIO.PWM(11, 50) 
p_fwd   = GPIO.PWM(13, 50) 
p_left  = GPIO.PWM(8, 50)  
p_right = GPIO.PWM(10, 50) 

p_cam_lr  = GPIO.PWM(15, 50) 
p_cam_ud   = GPIO.PWM(18, 50) 

p_cam_lr.start(0)
p_cam_ud.start(0)
p_left.start(0)
p_right.start(0)
p_back.start(0)
p_fwd.start(0)

#Create a socket connection for connecting to the server:
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

dd = 9
z_last = 0
y_last = 0
x_last = 0
while True:
    #Recieve data from the server:
    data = client_socket.recv(1024).split(",")
    #print "length",str(len(data))
    x = int(data[0])
    y = int(data[1])
    z = int(data[2])
    throttle = int(data[3])
    #hat= int(data[4])
    # for now, anything larger than 100 for x is our signal to exit
    if (x > 100): 
        print "getting command to exit"
        break
    if (y != y_last):
        if (y < -1*dd):
            p_fwd.ChangeDutyCycle(-1.0*y)
            p_back.ChangeDutyCycle(0)
        elif (y > dd):
            p_back.ChangeDutyCycle(1.0*y)
            p_fwd.ChangeDutyCycle(0)
        else:
            y = 0
            p_fwd.ChangeDutyCycle(0)
            p_back.ChangeDutyCycle(0)
            
    if (x != x_last):
        if (x < -1*dd):
            p_right.ChangeDutyCycle(-1.0*x)      
            p_left.ChangeDutyCycle(0)      
        elif (x > dd):
            p_left.ChangeDutyCycle(1.0*x)      
            p_right.ChangeDutyCycle(0)      
        else:
            x = 0
            p_right.ChangeDutyCycle(0)      
            p_left.ChangeDutyCycle(0)      

    if (z != z_last):
        if ((z < -1*dd) or (z > dd)):
            print "changing z"
            p_cam_lr.ChangeDutyCycle(abs(z-100)/15)
        else:
            #z = 0
            if (z_last != 0):
                print "changing z"
                p_cam_lr.ChangeDutyCycle(6.67)



    #p_cam_ud.ChangeDutyCycle(abs(z))
    #p_cam_lr.ChangeDutyCycle(abs(throttle))
    x_last = x
    y_last = y
    z_last = z
    print "(", x,", ", y,",",z,",",throttle,")"
  
print "closing client connection"
client_socket.close()
