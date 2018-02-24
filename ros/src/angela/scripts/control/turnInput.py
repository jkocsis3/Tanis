#!/usr/bin/env python

'''
**********************************************************************
* Filename    : turnInput.py
* Description : takes gamepad commands and sends messages.
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''

import rospy
from evdev import InputDevice, categorize, ecodes
from angela.msg import steermsg


class TurnInput(object):
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "turnInput.py":'

    def __init__(self, debug=False):
        self._DEBUG = debug
        # implement ROS subscribers
        rospy.init_node('Turn_Node')
        rospy.loginfo(self._DEBUG_INFO + "initalizing node")

        self.pub_steer = rospy.Publisher('/angela/steer/setAngle', steermsg, queue_size=5)
        self.turningValue = 90  
        self.rate = rospy.Rate(10)
        # time.sleep(10)
        self.controller = InputDevice('/dev/input/event0')
        
        # while ROS is running
        while not rospy.is_shutdown():
            # self.controller.grab()
            self.ReadInputs()
            # self.controller.ungrab()


    def ReadInputs(self):
        for event in self.controller.read_loop():
            try:
                if event.type == ecodes.EV_ABS:
                    absevent = categorize(event)            
                    if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_X':                    
                        self.turningValue = (90 + (float(absevent.event.value) / 1050)) / 18 + 2
                        # self.turningValue = self.SetPWM(self.turningValue)
                        if self._DEBUG:
                            rospy.loginfo(self._DEBUG_INFO + " turning value = " + str(float(self.turningValue)))
                        self.pub_steer.publish(self.turningValue)
                        break            
            except IOError:
                pass
        rospy.loginfo("sleeping")
        self.rate.sleep()

    def SetPWM(self, angle):
        return angle / 18 + 2
            
if __name__ == '__main__':
    TurnInput()
