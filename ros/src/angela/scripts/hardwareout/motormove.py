#!/usr/bin/env python

'''
**********************************************************************
* Filename    : motormove.py
* Description : A driver to move wheels forward and back. This is used
                in my self driving R/C car "tanis" as the basic module
                to drive the car
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''
from SunFounder_TB6612 import TB6612
import RPi.GPIO as GPIO
import rospy
from angela.msg import motormsg
_DEBUG = True
_DEBUG_INFO = 'DEBUG "motormove.py":'

class MotorMove():
    def __init__(self):
        if _DEBUG:
            rospy.loginfo(_DEBUG_INFO + " initializing node")
        GPIO.setmode(GPIO.BCM)
        # set GPIO22 and GPIO27 (pins 13 and 15)
        GPIO.setup((27, 22), GPIO.OUT)
        # make the motor objects and assign the frequency.
        self.a = GPIO.PWM(27, 60)
        self.b = GPIO.PWM(22, 60)

        self.motorA = TB6612.Motor(6)
        self.motorB = TB6612.Motor(13)

        self.motorA.debug = True
        self.motorB.debug = True

        self.delay = 0.05
        # start the motor with a duty cycle of 0, basically it is off.  
        self.startMotor(0)

        # implement ROS subscribers
        rospy.init_node('MotorMove')
        self.speed_sub = rospy.Subscriber('/angela/motor/setSpeed', motormsg, self.move)
        # stops the node from exiting
        rospy.spin()

    def moveForward(self, rate):
        if _DEBUG:
            rospy.loginfo(_DEBUG_INFO + " motors moving forward at:" + str(rate))
        self.motorA.forward()
        self.motorA.speed = rate
        self.motorB.forward()
        self.motorB.speed = rate

    def moveBackward(self, rate):
        if _DEBUG:
            rospy.loginfo(_DEBUG_INFO + " motors moving backward at:" + str(rate))
        self.motorA.backward()
        self.motorA.speed = rate
        self.motorB.backward()
        self.motorB.speed = rate

    # Main function to move the motors.
    # takes a rate(0-100) and a direction 1 (forward), 0(Full stop_ or -1(reverse)
    def move(self, data):
        if data.direction == 1:
            self.moveForward(rate=data.rate)
        elif data.direction == -1:
            self.moveBackward(rate=data.rate)
        else:
           self.stop()

    def startMotor(self, rate):
        self.a.start(0)
        self.b.start(0)

        def a_speed(value):
            self.a.ChangeDutyCycle(value)

        def b_speed(value):
            self.b.ChangeDutyCycle(value)

        self.motorA.pwm = a_speed
        self.motorB.pwm = b_speed
        # self.moveForward(rate)

    def stop(self):
        self.motorA.stop()
        self.motorB.stop()
if __name__ == '__main__':
  MotorMove()
