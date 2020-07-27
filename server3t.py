import RPi.GPIO as GPIO
import time
import socket
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

def lighton(lnoa):
    GPIO.output(lnoa,True)
    lstatus[int(lno)]=1

def lightoff(lnoa):
     GPIO.output(lnoa,False)
     lstatus[int(lno)]=0
      
def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    return s.getsockname()[0]
    
def lightcontrol(lno,on):
	
    if on == 1:
	    lighton(lname[lno])
	    print "light on"
	
    elif on == 0:
		lightoff(lname[lno])

HOST = "192.168.43.159"
PORT = 2600
 
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

lstatus=[0,0,0,0]
lname=[0,3,4,17]
lno=0
lnoa=0

while 1:
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
     
    reply = 'Yes'
     
    s.sendto(reply , addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
    
    list(data)
    com=int(data[0])
    arg=data[1]
    arg2=data[2]
    
    if com==1:                                 #light control
	    lightcontrol(int(arg),int(arg2))
	    print "hi"
    if com==2:                                 #alarm
		os.system("python wheather1.py")
    
    
    
s.close()
