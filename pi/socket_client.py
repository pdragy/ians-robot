#!/usr/bin/env python 

import sys, socket
import time
#import RPi.GPIO as GPIO

import string,  serial

device_name = '/dev/ttyACM0'
baud_rate = 9600

t_final = 50
ser = serial.Serial(device_name, baud_rate)
#ser = open('test_output.txt', 'r')
if (len(sys.argv) < 3):
    print "expected server ip address and port number"
    print "example: socket_client.py 192.168.1.118 5001"
    exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])
#Create a socket connection for connecting to the server:
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

dd = 9
y_last = 0
x_last = 0
y = 0
x = 0
y_car = 0
x_car = 0
while True:
    #Recieve data from the server:
    data = client_socket.recv(1024).split(",")
    #while (len(data) < 2):
    #    time.sleep(100)
    x = int(data[0])
    y = int(data[1])
    #y_car = int((y + 100)/10.0 + 83)
    #x_car = int((x + 100)/200.0 * 179)
    y_car = int(((y + 100)/200.0)*255)
    x_car = int(((x + 100)/200.0)*255)

    ser.write('0')
    ser.write(chr(y_car))
    ser.write(chr(x_car))
    ser.write('1')
    ser.write('1')
    # for now, anything larger than 100 for x is our signal to exit
    if (x > 100): 
        print "getting command to exit"
        break
    x_last = x
    y_last = y
    #print "(", x,", ", y,")"
    print "(", x_car,", ", y_car,")"
    #time.sleep(0.05)
  
print "closing client connection"
client_socket.close()
