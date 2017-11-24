#!/usr/bin/env python

'''
**********************************************************************
* Filename    : joystick.py
* Description : takes gamepad commands and sends messages.
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''

import rospy
from evdev import InputDevice, categorize, ecodes
from angela.msg import motormsg, steermsg
import time
class JoyStick(object):
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "JoyStick.py":'

    def __init__(self, debug=True):
        self.DEBUG = debug
         # implement ROS subscribers
        rospy.init_node('JoyStick')
        self.pub_speed = rospy.Publisher('/angela/motor/setSpeed', motormsg, queue_size=10)
        self.pub_steer = rospy.Publisher('/angela/steer/setAngle', steermsg, queue_size=10)
        self.speed = 0  
        self.turningValue = 90  
        self.rate = rospy.Rate(5)
        # time.sleep(10)
        self.controller = InputDevice('/dev/input/event0')
         # while ROS is running
        while not rospy.is_shutdown():
            self.ReadInputs()



    def ReadInputs(self):
        for event in self.controller.read_loop():
            if event.type == ecodes.EV_ABS:
                absevent = categorize(event)
                if self._DEBUG:
                    rospy.loginfo(self._DEBUG_INFO + " Event telemetry received")
                if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RZ':
                    self.speed = absevent.event.value / 10.23
                    if self.speed <0:
                        self.speed = 0
                    if self.speed > 100:
                        self.speed = 100
                    self.pub_speed.publish(abs(int(self.speed)), 1)

                if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_X':                    
                    self.turningValue = 90 + int(absevent.event.value / 1050) 
                    if self._DEBUG:
                        rospy.loginfo(self._DEBUG_INFO + " turning value = " + str(int(self.turningValue)))
                    self.pub_steer.publish(self.turningValue)
            self.rate.sleep()
                # print(absevent.event.type)
if __name__ == '__main__':
    JoyStick()
       