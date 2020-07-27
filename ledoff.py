import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17 , GPIO.OUT)


GPIO.output(3, False)
GPIO.output(4, False)
GPIO.output(17, False)

    
