#!/usr/local/bin/python

import string, sys, serial, time

device_name = '/dev/ttyACM0'
baud_rate = 9600
output_file = "mind_output.txt"

t_final = 60
ser = serial.Serial(device_name, baud_rate)
#ser = open('test_output.txt', 'r')

for t in range(t_final):
    ser.write(str(t*2))
    print(t*2)
    time.sleep(1)
