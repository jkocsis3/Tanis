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
from angela.msg import motormsg
class JoyStick(object):
    DEBUG = True;
    def __init__(self, debug=True):
        DEBUG = debug
         # implement ROS subscribers
        rospy.init_node('JoyStick')
        self.pub_speed = rospy.Publisher('/angela/motor/setSpeed', motormsg, queue_size=10)
        
        self.speed = 0    
         # while ROS is running
        while not rospy.is_shutdown():
            self.ReadInputs()



    def ReadInputs(self):
        gamepad = InputDevice('/dev/input/event0')
        for event in gamepad.read_loop():
            rospy.loginfo("Reading event telemetry")
            if event.type == ecodes.EV_ABS:
                absevent = categorize(event)
                rospy.loginfo("event type " + str(event))
                if absevent.event.type == 3:
                    self.speed = absevent.event.value / 10.23
                    if self.speed <0:
                        self.speed = 0
                    self.pub_speed.publish(abs(int(self.speed)), 1)
                    rospy.loginfo("speed = " + str(int(self.speed)))
                
                # print(absevent.event.type)
if __name__ == '__main__':
    JoyStick()
       