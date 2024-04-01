import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.OUT)
servo=GPIO.PWM(33, 50)

servo.start(0)

def SetAngle(angle):
	duty = angle / 18 +2
	GPIO.output(33, True)
	servo.ChangeDutyCycle(duty)
	print(duty)

while True:
	a=input("enter value : ")
	a=int(a)
	SetAngle(a)

servo.stop()
GPIO.cleanup()
