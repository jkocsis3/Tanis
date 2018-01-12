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

from PWM_Control import PCA9685
from smbus import SMBus
import time


class Steer(object):    

    def __init__(self, debug=True):  
        # Set our limits. there are about 30 degrees of movement on each side of center.
        self._maxangle = {"left": 60, "straight": 90, "right": 120}
   

    def turn(self, anglein):
        print("turning to: " + str(anglein))
        # http://www.python-exemplary.com/drucken.php?inhalt_mitte=raspi/en/servomotors.inc.php
        fPWM = 50
        i2c_address = 0x40  # (standard) adapt to your module
        channel = 8  # adapt to your wiring
        a = 5.5  # adapt to your servo
        b = 2   # adapt to your servo

        bus = SMBus(1)  # Raspberry Pi revision 2
        pwm = PCA9685.PWM(bus, i2c_address)
        pwm.setFreq(fPWM)

        i = 0
        while i < 180:
            anglein = i
            duty = a / 180 * anglein + b
            pwm.setDuty(channel, duty)
            print("direction =" + str(anglein) + "-> duty =" + str(duty))
            # time.sleep(1)  # allow to settle
            i+=1
        print("turn complete")


    def SetAngle(self, angle):
        return angle / 18 + 2

if __name__ == '__main__':
    Steer()
