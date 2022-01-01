import socket          
 
s = socket.socket()        
print ("Socket successfully created")

ip="192.168.10.4"
port = 12345               
 
s.bind((ip, port))        
print ("socket binded to %s" %(port))
 
s.listen(5)    
print ("socket is listening")           
 
while True:
  c, addr = s.accept()    
  print ('Got connection from', addr )
  msg=c.recv(1024).decode()
  print(msg[2:])
 
  c.send('Thank you for connecting'.encode())
  c.close()
