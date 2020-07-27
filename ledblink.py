import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

while(True):
    GPIO.output(3, False)
    GPIO.output(4, True)
    GPIO.output(17, False)
    time.sleep(0.5)
    GPIO.output(3, True)
    GPIO.output(4, False)
    GPIO.output(17, True)
    time.sleep(0.5)
    
