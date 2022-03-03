import socket                

s = socket.socket()
port = 12346     # Define the port on which you want to connect
s.connect(('127.0.0.1', port))   # Connect to the server on local computer
print(s.recv(1024))   # Receive data from the server 
s.close()
