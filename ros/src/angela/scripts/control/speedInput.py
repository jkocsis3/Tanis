#!/usr/bin/env python

'''
**********************************************************************
* Filename    : speedInput.py
* Description : takes speed commands from game pad.
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''

import rospy
from evdev import InputDevice, categorize, ecodes
from angela.msg import motormsg


class SpeedInput(object):
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "speedInput.py2":'

    def __init__(self, debug=True):
        self.DEBUG = debug
        # implement ROS subscribers
        rospy.init_node('SpeedInput')
        rospy.loginfo(self._DEBUG_INFO + "initalizing node")
        self.pub_speed = rospy.Publisher('/angela/motor/setSpeed', motormsg, queue_size=10)
        self.speed = 0  
        self.rate = rospy.Rate(50)
        self.controller = InputDevice('/dev/input/event0')
        # while ROS is running
        while not rospy.is_shutdown():
            self.ReadInputs()

    def ReadInputs(self):
        for event in self.controller.read_loop():
            try:            
                if event.type == ecodes.EV_ABS:
                    absevent = categorize(event)
                    if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RZ':
                        self.speed = absevent.event.value / 10.23
                        if self.speed < 0:
                            self.speed = 0
                        if self.speed > 100:
                            self.speed = 100
                        self.pub_speed.publish(abs(int(self.speed)), "forward")
                        rospy.loginfo(self._DEBUG_INFO + " Forward Speed value - BLARG = " + str(abs(int(self.speed))))  
                    if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z':
                        self.speed = absevent.event.value / 10.23
                        if self.speed < 0:
                            self.speed = 0
                        if self.speed > 100:
                            self.speed = 100
                        self.pub_speed.publish(abs(int(self.speed)), "reverse")
                        rospy.loginfo(self._DEBUG_INFO + "Reverse Speed value = " + str(abs(int(self.speed))))                  
                # self.rate.sleep()
            except IOError:
                pass
            
if __name__ == '__main__':
    SpeedInput()
