import RPi.GPIO as GPIO
import time

BuzzerPin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT) 

global Buzz
Buzz = GPIO.PWM(BuzzerPin, 440)
Buzz.start(10) 

x = 1500
while(x<3000):
  Buzz.ChangeFrequency(x)
  time.sleep(0.01)
  x+=40
  
while(x>2000):
  Buzz.ChangeFrequency(x)
  time.sleep(0.05)
  x-=20
Buzz.start(0)
