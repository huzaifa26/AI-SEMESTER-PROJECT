import socket
import serial
 
s = socket.socket()        
print ("Socket successfully created")

ip="192.168.10.4"
port = 12345               
 
s.bind((ip, port))        
print ("socket binded to %s" %(port))
 
s.listen(5)    
print ("socket is listening")

# Connecting to the Arduino serial port
try:
    usb = serial.Serial("/dev/ttyUSB0", 9600, timeout=2)
    print("Connected To Serial port")
except:
    print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
    exit()
 
while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    msg=c.recv(1024).decode()
    message=msg[2:]
    
    if message == "START" and message != "":
        try:
            usb.write(b'START')
            print("STARTING THE CAR")
        except:
            print("Couln't Start the car")
    elif message == "STOP" and message != "":
        try:
            usb.write(b'STOP')
            print("STOPPING THE CAR")
        except:
            print("Couldn't stop the car")
        
    c.close()