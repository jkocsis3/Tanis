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



class Steer(object):

    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "steer.py":'

    def __init__(self, debug=True):  
        self._DEBUG = debug
        
        if self._DEBUG:
            rospy.loginfo("Launching steer script")       
        
        # Set our limits. there are about 30 degrees of movement on each side of center.
        self._maxangle = {"left": 60, "straight": 90, "right": 120}
        if self._DEBUG:
            rospy.loginfo(self._DEBUG_INFO + 'left angle: %s, straight angle: %s, right angle: %s' % (self._maxangle["left"], self._maxangle["straight"], self._maxangle["right"]))

        # implement ROS subscribers
        rospy.init_node('SteeringNode')
        self.speed_sub = rospy.Subscriber('/angela/steer/setAngle', steermsg, self.turn)
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
        duty = self.SetAngle(anglein)
        pwm.setDuty(channel, duty)
        if self._DEBUG:
            rospy.loginfo("script complete")

    def SetAngle(self, angle):
        return angle / 18 + 2


if __name__ == '__main__':
    Steer()
