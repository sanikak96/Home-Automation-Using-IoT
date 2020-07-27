import RPi.GPIO as GPIO
import time
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
     
lstatus=[0,0,0,0]
lname=[0,3,4,17]
while(True): 
    
    
    print "lstatus"
    print lstatus
    print "lname"
    print lname
    lno=0
    lnoa=0
    lno=int(raw_input("enter the light no. \n you would like to turn on the light??" ))
    lighton(lname[lno])
    lno=int(raw_input("enter the light no. \n you would like to turn off the light??" ))
    lightoff(lname[lno])
