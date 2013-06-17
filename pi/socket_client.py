import  sys, socket

port = 5000
ip = "192.168.0.118"

#Create a socket connection for connecting to the server:
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

while True:
   #Recieve data from the server:
   data = client_socket.recv(1024)
   print data
   
socket.close()
