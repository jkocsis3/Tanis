#!/usr/bin/env python

'''
**********************************************************************
* Filename    : tanisTest.py
* Description : Test script for various parts of the car.
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''

import time
import rospy
from angela.msg import motormsg, steermsg


class TanisTest(object):
    """docstring for TanisTest"""
    def __init__(self):
        self._verbose = True
        # we will be publishing messages on the setSpeed topic for the motor to sub to
        self.pub_speed = rospy.Publisher('/angela/motor/setSpeed', motormsg, queue_size=10)
        self.pub_steer = rospy.Publisher('/angela/steer/setAngle', steermsg, queue_size=10)
        # initialize the tanisTest node, this must be done before any other rospy package functions are called
        rospy.init_node("tanisTest")

        if self._verbose:
            rospy.loginfo("Started the Test Node")

        self.rate = rospy.Rate(10)
        self.targetSpeed = 100
        self.steerAngle = 90
        self.direction = 'right'

        # while ROS is running
        while not rospy.is_shutdown():
            self.TestSpeed()
            self.TestSteer()

    def TestSpeed(self):
        if self._verbose:
            rospy.loginfo("Current Speed = " + str(self.targetSpeed))
        self.pub_speed.publish(self.targetSpeed, 1)
        time.sleep(5)
        print("stopping motors")
        self.targetSpeed = 0
        self.pub_speed.publish(self.targetSpeed, 1)

    def TestSteer(self):
        if self._verbose:
            rospy.loginfo("Current Steering Angle = " + str(self.steerAngle) + " Direction of Turn = " + str(self.direction))
        self.pub_steer.publish(self.steerAngle)
        time.sleep(5)

        self.steerAngle = 60
        if self._verbose:
            rospy.loginfo("Current Steering Angle = " + str(self.steerAngle) + " Direction of Turn = " + str(self.direction))
        self.pub_steer.publish(self.steerAngle)
        time.sleep(5)
        self.steerAngle = 120
        if self._verbose:
            rospy.loginfo("Current Steering Angle = " + str(self.steerAngle) + " Direction of Turn = " + str(self.direction))
        self.pub_steer.publish(self.steerAngle)
        time.sleep(5)
        self.steerAngle = 90
        if self._verbose:
            rospy.loginfo("Current Steering Angle = " + str(self.steerAngle) + " Direction of Turn = " + str(self.direction))
        self.pub_steer.publish(self.steerAngle)
        




if __name__ == '__main__':
    try:
        TanisTest()
    except rospy.ROSInterruptException:
        pass
