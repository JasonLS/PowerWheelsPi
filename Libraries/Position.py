import Motors
import Servo
import time

def turnRight():
	Motors.still()
	Servo.turn_right()
	Motors.forward()
	time.sleep(3)
	Motors.still()
	Servo.center()

def turnLeft():
	Motors.still()
	Servo.turn_left()
	Motors.forward()
	time.sleep(3)
	Motors.still()
	Servo.center()

def turnAround():
	Motors.still()
	Servo.turn_right()
	Motors.forward()
	time.sleep(6)
	Motors.still()
	Servo.center()

turnRight()
time.sleep(1)
turnLeft()
time.sleep(1)
turnAround()
