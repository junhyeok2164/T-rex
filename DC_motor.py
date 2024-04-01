import RPi.GPIO as GPIO
from time import sleep

Motor1A = 7
Motor1B = 8
Motor1E = 25
Motor2A = 18
Motor2B = 15
Motor2E = 14 


def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Motor1A, GPIO.OUT)
	GPIO.setup(Motor1B, GPIO.OUT)
	GPIO.setup(Motor1E, GPIO.OUT)
	GPIO.setup(Motor2A, GPIO.OUT)
	GPIO.setup(Motor2B, GPIO.OUT)
	GPIO.setup(Motor2E, GPIO.OUT)

	DCM1=GPIO.PWM(Motor1E, 100)
	DCM2=GPIO.PWM(Motor2E, 100)
	DCM1.start(0)
	DCM2.start(0)

def loop():
	GPIO.output(Motor1A, GPIO.HIGH)
	GPIO.output(Motor1B, GPIO.LOW)
	GPIO.output(Motor1E, GPIO.HIGH)
	GPIO.output(Motor2A, GPIO.HIGH)
	GPIO.output(Motor2B, GPIO.LOW)
	GPIO.output(Motor2E, GPIO.HIGH)
	DCM1.ChangeDutyCycle(50)	#Change the speed of motor1
	DCM2.ChangeDutyCycle(50)
	print("Going Forwards")
	
	sleep(5)
	GPIO.output(Motor1E, GPIO.LOW)
	GPIO.output(Motor1B, GPIO.LOW)
	GPIO.output(Motor2E, GPIO.LOW)
	GPIO.output(Motor2B, GPIO.LOW)
	print("Stop")
	
def destroy():
	GPIO.cleanup()
	
if __name__ == '__main__':
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Motor1A, GPIO.OUT)
	GPIO.setup(Motor1B, GPIO.OUT)
	GPIO.setup(Motor1E, GPIO.OUT)
	GPIO.setup(Motor2A, GPIO.OUT)
	GPIO.setup(Motor2B, GPIO.OUT)
	GPIO.setup(Motor2E, GPIO.OUT)

	DCM1=GPIO.PWM(Motor1E, 100)
	DCM2=GPIO.PWM(Motor2E, 100)
	DCM1.start(0)
	DCM2.start(0)
	try:
		GPIO.output(Motor1A, GPIO.HIGH)
		GPIO.output(Motor1B, GPIO.LOW)
		GPIO.output(Motor1E, GPIO.HIGH)
		GPIO.output(Motor2A, GPIO.HIGH)
		GPIO.output(Motor2B, GPIO.LOW)
		GPIO.output(Motor2E, GPIO.HIGH)
		DCM1.ChangeDutyCycle(100)	#Change the speed of motor1
		DCM2.ChangeDutyCycle(100)
		print("Going Forwards")
		
		sleep(20)
		GPIO.output(Motor1A, GPIO.HIGH)
		GPIO.output(Motor1B, GPIO.LOW)
		GPIO.output(Motor1E, GPIO.HIGH)
		GPIO.output(Motor2A, GPIO.HIGH)
		GPIO.output(Motor2B, GPIO.LOW)
		GPIO.output(Motor2E, GPIO.HIGH)
		DCM1.ChangeDutyCycle(50)	#Change the speed of motor1
		DCM2.ChangeDutyCycle(50)
		print("Going Forwards")
		
		sleep(5)
		GPIO.output(Motor1E, GPIO.LOW)
		GPIO.output(Motor1B, GPIO.LOW)
		GPIO.output(Motor2E, GPIO.LOW)
		GPIO.output(Motor2B, GPIO.LOW)
		print("Stop")
	except KeyboardInterrupt:
		destroy()
