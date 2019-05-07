#Raspberry Pi Motion Detector Code 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) 


while True:
  if GPIO.input(23): #If there is a movement, PIR sensor gives input to GPIO 23
     GPIO.output(24, True) #Output given to Buzzer through GPIO 24  
     time.sleep(1) #Buzzer turns on for 1 second
     GPIO.output(24, False)
     time.sleep(5) 
  time.sleep(0.1) 