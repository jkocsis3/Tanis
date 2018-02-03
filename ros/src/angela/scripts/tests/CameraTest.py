#!/usr/bin/env python

'''
**********************************************************************
* Filename    : cameraTest.py
* Description : tests the images coming in from the camera
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''
import rospy
from sensor_msgs.msg import Image
import cv2


class CameraTest(object):
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "CameraTest.py2":'

    def __init__(self, debug=True):
        rospy.initnode("CameraTest")
        self.image_sub = rospy.Subscriber("/angela/cameras/main/capture", Image, self.imageCallback)
        rospy.spin


    def imageCallback(self, data):
        image = data
