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
# from angela.msg import steermsg


class Steer(object):

    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "steer.py":'

    def __init__(self, debug=True):  
        # if self._DEBUG:
        #     rospy.loginfo("Launching steer script")       
        
        self._DEBUG = debug
        
        # Set our limits. there are about 30 degrees of movement on each side of center.
        self._maxangle = {"left": 60, "straight": 90, "right": 120}
        # if self._DEBUG:
        #     rospy.loginfo(self._DEBUG_INFO + 'left angle: %s, straight angle: %s, right angle: %s' % (self._maxangle["left"], self._maxangle["straight"], self._maxangle["right"]))

        # implement ROS subscribers
        # rospy.init_node('SteeringNode')
        # self.speed_sub = rospy.Subscriber('/angela/steer/setAngle', steermsg, self.turn)
        # # stops the node from exiting
        # rospy.spin()
   

    def turn(self, angle):
        ''' Turn the front wheels to the given angle '''
        # set the mode to broadcom (Use GPO numbers not pin numbers)      
        # http://www.instructables.com/id/Servo-Motor-Control-With-Raspberry-Pi/
        gpioNum = 26
        GPIO.setmode(GPIO.BCM)
        # set GPIO18 as an output
        GPIO.setup(gpioNum, GPIO.OUT)
        # make the servo object and assign the frequency.
        servo = GPIO.PWM(gpioNum, 60)
        # start the servo with a 0 duty cycle
        servo.start(0)  
        anglein = angle      
        # if self._DEBUG:
        #     rospy.loginfo("Turn to: " + str(anglein))
        print("Turn to: " + str(anglein))
        
        if anglein < self._maxangle["left"]:
            anglein = self._maxangle["left"]
        if anglein > self._maxangle["right"]:
            anglein = self._maxangle["right"]

        angle = self.SetAngle(anglein)
        # turn the pin on
        GPIO.output(gpioNum, True)
        # send the command
        servo.ChangeDutyCycle(angle)
        # allow the servo to complete movement.
        time.sleep(1)
        servo.stop()
        # change back to 0 so we are not sending inputs
        # servo.ChangeDutyCycle(0)

        # turn the pin off
        GPIO.output(gpioNum, False)
        

        GPIO.cleanup()
        # if self._DEBUG:
        #     rospy.loginfo("script complete")

  

    def SetAngle(self, angle):
        return angle / 18 + 2


if __name__ == '__main__':
    Steer()
