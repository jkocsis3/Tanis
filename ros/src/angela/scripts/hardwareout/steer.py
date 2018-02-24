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
from smbus import SMBus
import rospy
from angela.msg import steermsg
from PWM_Control import PCA9685
import numpy as np
from collections import deque



class Steer(object):

    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "steer.py":'

    def __init__(self, debug=False):  
        self._DEBUG = debug 

        rospy.init_node('Steering_Node')
        rospy.loginfo(self._DEBUG_INFO + "initalizing node")       
        
        # Set our limits. there are about 30 degrees of movement on each side of center.
        self._maxangle = {"left": 5, "straight": 6.8, "right": 8}        

       
        self.speed_sub = rospy.Subscriber('/angela/steer/setAngle', steermsg, self.turn)
        self.steeringAverage = deque(maxlen=10)
        # stops the node from exiting
        rospy.spin()
   

    def turn(self, data):
        ''' Turn the front wheels to the given angle '''
        anglein = data.angle      
        if self._DEBUG:
            rospy.loginfo("Turn to: " + str(anglein))
        
        if anglein < self._maxangle["left"]:
            anglein = self._maxangle["left"]
        if anglein > self._maxangle["right"]:
            anglein = self._maxangle["right"]
        # http://www.python-exemplary.com/drucken.php?inhalt_mitte=raspi/en/servomotors.inc.php
        fPWM = 50
        i2c_address = 0x40  # (standard) adapt to your module
        channel = 15  
        bus = SMBus(1)  
        pwm = PCA9685.PWM(bus, i2c_address)
        pwm.setFreq(fPWM)

        # get the average of the last 10 inputs to the array
        offset = -0.30
        anglein = anglein + offset
        self.steeringAverage.append(anglein)
        avgAngle = sum(self.steeringAverage) / float(len(self.steeringAverage))
        # np.insert(self.steeringAverage, 9, anglein)

        if self._DEBUG:
            rospy.loginfo(self.steeringAverage)        

        if self._DEBUG:
            rospy.loginfo("avg angle: " + str(avgAngle))

        
        pwm.setDuty(channel, anglein)
        if self._DEBUG:
            rospy.loginfo("script complete")

    


if __name__ == '__main__':
    Steer()
