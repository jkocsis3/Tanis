#!/usr/bin/env python

'''
**********************************************************************
* Filename    : steer.py
* Description : A driver to steer the front wheels left and right. 
                This is used in my self driving R/C car "tanis" 
                as the basic module to steer the car
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''
import sys
import time
import RPi.GPIO as GPIO
import rospy
from angela.msg import steermsg


class Steer(object):

    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "steer.py":'

    def __init__(self, debug=True, bus_number=1):  
        # set the mode to broadcom (Use GPO numbers not pin numbers)      
        GPIO.setmode(GPIO.BCM)
        # set GPIO18 as an output
        GPIO.setup((18), GPIO.OUT)
        # make the servo object and assign the frequency.
        self.servo = GPIO.PWM(18, 60)

        # start the servo with a 0 duty cycle
        self.servo.start(0)
        self.SetAngle(90)
        self.servo.stop()
        GPIO.cleanup()
        
        self._DEBUG = debug
        
        # Set our limits. there are about 30 degrees of movement on each side of center.
        self._maxangle = {"left":60, "straight":90, "right":120}
        if self._DEBUG:
            rospy.loginfo(self._DEBUG_INFO + 'left angle: %s, straight angle: %s, right angle: %s' % (self._maxangle["left"], self._maxangle["straight"], self._maxangle["right"]))

        # implement ROS subscribers
        rospy.init_node('SteeringNode')
        self.speed_sub = rospy.Subscriber('/angela/steer/setAngle', steermsg, self.turn)
        # stops the node from exiting
        rospy.spin()
   
    '''
        Takes an angle, checks it against the limits, performs the turn
    '''
    def turn(self, data):
        ''' Turn the front wheels to the given angle '''

        # set the mode to broadcom (Use GPO numbers not pin numbers)      
        GPIO.setmode(GPIO.BCM)
        # set GPIO18 as an output
        GPIO.setup((18), GPIO.OUT)
        angle = self.SetAngle(data.angle)
        if self._DEBUG:
            rospy.loginfo(self._DEBUG_INFO + "Turn to" + str(angle))
        if angle < self._maxangle["left"]:
            angle = self._maxangle["left"]
        if angle > self._maxangle["right"]:
            angle = self._maxangle["right"]
        # turn the pin on
        GPIO.output(18, True)
        # send the command
        self.servo.ChangeDutyCycle(angle)
        # allow the servo to complete movement.
        time.sleep(1)
        # turn the pin off
        GPIO.output(18, False)
        # change back to 0 so we are not sending inputs
        self.servo.ChangeDutyCycle(0)

    def SetAngle(self, angle):
        return angle / 18 + 2
if __name__ == '__main__':
    Steer()
       