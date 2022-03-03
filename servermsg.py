import socket                

s = socket.socket()          
print("Socket successfully created")
port = 12346     # Reserve a port on your computer...in our case it is 12345, but it can be anything
s.bind(('', port))         
print("Socket binded to %s" %(port))
s.listen(5)    # Put the socket into listening mode       
print("Socket is listening")            

while True:
  c, addr = s.accept()   # Establish connection with client
  print('Got connection from', addr)
  c.send('Thank you for connecting'.encode('utf-8'))   # Send a message to the client
  c.close()
