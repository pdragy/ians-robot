import  sys, socket
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Do we need these or did we make these always on?
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.output(3,1) 
GPIO.output(5, 1)
GPIO.output(7, 1)

# set up the PWM pins for left/right forward/back control
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

p_back = GPIO.PWM(11, 50) 
p_fwd = GPIO.PWM(13, 50) 
p_left = GPIO.PWM(8, 50)  
p_right = GPIO.PWM(10, 50) 

p_left.start(0)
p_right.start(0)
p_back.start(0)
p_fwd.start(0)

port = 5000
ip = "192.168.1.118"

#Create a socket connection for connecting to the server:
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

while True:
    #Recieve data from the server:
    data = client_socket.recv(1024)
    data2 = data.split( ",")
    x = int(data2[0])
    y = int(data2[1])
    if (y < -5):
        p_fwd.ChangeDutyCycle(-1.0*y)
        p_back.ChangeDutyCycle(0)
    elif (y > 5):
        p_back.ChangeDutyCycle(1.0*y)
        p_fwd.ChangeDutyCycle(0)
    else:
        p_fwd.ChangeDutyCycle(0)
        p_back.ChangeDutyCycle(0)
        
    if (x < -5):
        p_right.ChangeDutyCycle(-1.0*x)      
        p_left.ChangeDutyCycle(0)      
    elif (x > 5):
        p_left.ChangeDutyCycle(1.0*x)      
        p_right.ChangeDutyCycle(0)      
    else:
        p_right.ChangeDutyCycle(0)      
        p_left.ChangeDutyCycle(0)      

    print x,y
   
client_socket.close()
