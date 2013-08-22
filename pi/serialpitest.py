#!/usr/local/bin/python

import string, sys, serial, time

device_name = '/dev/ttyACM0'
baud_rate = 9600

t_final = 50
ser = serial.Serial(device_name, baud_rate)
#ser = open('test_output.txt', 'r')

for t in range(4,t_final):
    ser.write('0')
    ser.write(chr(1))
    ser.write(chr(3))
    ser.write(chr(7))
    ser.write(chr(111))
    print(t)
    time.sleep(0.1)
