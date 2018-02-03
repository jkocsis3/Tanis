#!/usr/bin/env python

'''
**********************************************************************
* Filename    : camerain.py
* Description : Captures images from Pi Camera
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''

import picamera
import picamera.array
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from picamera.array import PiRGBArray


class Camera():
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "camCapture.py2":'

    def __init__(self, debug=False):
        self._DEBUG = debug
        if self._DEBUG:
            rospy.loginfo(self._DEBUG_INFO + " initializing node")

        rospy.init_node('Camera_Cap_Node')
        self.image_pub = rospy.Publisher("/angela/cameras/main/capture", Image, queue_size=10)
        
        self.rate = rospy.Rate(5)
        self.camera = picamera.PiCamera()
        while not rospy.is_shutdown():
            self.CaptureStill()            
            self.rate.sleep()

    def CaptureStill(self):        
        
        rawCapture = PiRGBArray(self.camera)
        self.camera.start_preview()
        # time.sleep(2)
        # https://answers.ros.org/question/199294/publish-image-msg/
        self.camera.capture(rawCapture, format='rgb')
        # self.camera.close()
        image = rawCapture.array
        # cv2image = cv2.imread(image)
        msgImage = CvBridge().cv2_to_imgmsg(image, encoding="passthrough")
        self.image_pub.publish(msgImage)


if __name__ == '__main__':
    Camera()
