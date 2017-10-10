#!/usr/bin/env python
from SunFounder_TB6612 import TB6612
import RPi.GPIO as GPIO

class MotorMove():
	def __init__(self, rate, time):
		print("Begin setup")
		GPIO.setmode(GPIO.BCM)
		# set GPIO22 and GPIO27 (pins 13 and 15)
		GPIO.setup((27, 22), GPIO.OUT)
		# make the motor objects and assign the frequency.
		self.a = GPIO.PWM(27, 60)
		self.b = GPIO.PWM(22, 60)
		# start the motor with a duty cycle of 0, basically it is off. 
		

		self.motorA = TB6612.Motor(17)
		self.motorB = TB6612.Motor(18)
		self.motorA.debug = True
		self.motorB.debug = True
		self.delay = 0.05

		self.rate = rate
		self.time = time
		print("Starting motor")
		self.startMotor()

	def moveForward(self):
		print("motor A run")
		self.motorA.forward()
		self.motorA.speed = self.rate
		print("motor A run")
		self.motorB.forward()
		self.motorB.speed = self.rate


	def moveBackward(self):
		self.motorA.backward()
		self.motorA.speed = self.rate
		self.motorB.backward()
		self.motorB.speed = self.rate

	def stop(self):

		self.motorA.stop()
		self.motorB.stop()
		print("motors stopped")



	def startMotor(self):
		self.a.start(0)
		self.b.start(0)

		def a_speed(value):
			self.a.ChangeDutyCycle(value)

		def b_speed(value):
			self.b.ChangeDutyCycle(value)

		self.motorA.pwm = a_speed
		self.motorB.pwm = b_speed
		print("motor started")


	


if __name__ == '__main__':
	MotorMove()
