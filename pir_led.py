import RPi.GPIO as GPIO
import time

led1 = 17
led2 = 27
pirPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN)

def LIGHTS(pirPin):
    print("motion detected!")
    print("lights on")
    GPIO.output(led1,GPIO.HIGH)
    GPIO.output(led2,GPIO.HIGH)

    time.sleep(2)

    print("light off")
    GPIO.output(led1,GPIO.LOW)
    GPIO.output(led2,GPIO.LOW)

print("motion sensor alarm (CTRL+c to exit)")
time.sleep(.2)
print("ready")

try:
    GPIO.add_event_detect(pirPin, GPIO.RISING, callback=LIGHTS)
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    print("quit")
    GPIO.cleanup()


"""GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
//GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
//GPIO.setup(3, GPIO.OUT)         #LED output pin
//while True:
//    i=GPIO.input(11)
//if i==0:                 #When output from motion sensor is LOW
 //   print ("No intruders"),i
  //  GPIO.output(3, 0)  #Turn OFF LED
   // time.sleep(0.1)
//elif i==1:               #When output from motion sensor is HIGH
  //  print ("Intruder detected"),i
   // GPIO.output(3, 1)  #Turn ON LED
    //time.sleep(0.1)"""
