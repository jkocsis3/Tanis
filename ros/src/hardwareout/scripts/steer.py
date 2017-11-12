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


class Steer(object):

    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "steer.py":'

    def __init__(self, debug=True, bus_number=1):  
        # set the mode to broadcom (Use GPO numbers not pin numbers)      
        GPIO.setmode(GPIO.BCM)
        # set GPIO18 as an output
        GPIO.setup((18), GPIO.OUT)
        # make the servo object and assign the frequency.
        self.servo = GPIO.PWM(18, self._frequency)
        # start the servo with a 0 duty cycle
        self.servo.start(0)
        self.SetAngle(self.angle)
        self.servo.stop()
        GPIO.cleanup()

        
        self._DEBUG = debug
        if self._DEBUG:
            print self._DEBUG_INFO, 'Front wheel PWM channel:', self._channel
        # Set our limits. there are about 30 degrees of movement on each side of center.
        self._angle = {"left":60, "straight":90, "right":120}
        if self._DEBUG:
            print self._DEBUG_INFO, 'left angle: %s, straight angle: %s, right angle: %s' % (self._angle["left"], self._angle["straight"], self._angle["right"])

   
   
    '''
        Takes an angle, checks it against the limits, performs the turn
    '''
    def turn(self, angle):
        ''' Turn the front wheels to the giving angle '''
        angle = self.SetAngle(angle)
        if self._DEBUG:
            print self._DEBUG_INFO, "Turn to", angle
        if angle < self._angle["left"]:
            angle = self._angle["left"]
        if angle > self._angle["right"]:
            angle = self._angle["right"]
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
        