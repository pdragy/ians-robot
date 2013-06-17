import  sys, socket
import time
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create the socket
server_socket.bind(('', port)) # listen on port 5000
server_socket.listen(5) # queue max 5 connections
client_socket, address = server_socket.accept()

print "Your IP address is: ", socket.gethostbyname(socket.gethostname())
print "Server Waiting for client on port ", port

while True:
    # test string
    time.sleep(1)
    #data = bytearray('DEADBEEF'.decode('hex'))
    data = "foo"
    client_socket.sendall(data)
    
socket.close()
p.terminate()
