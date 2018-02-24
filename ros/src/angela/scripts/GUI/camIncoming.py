#!/usr/bin/env python

'''
**********************************************************************
* Filename    : camIncoming.py
* Description : receives the message for an image and processes it.
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import os


class CamIncoming():
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "camIncoming.py":'
    
    def __init__(self, debug=False):
        self._DEBUG = debug
        rospy.loginfo(self._DEBUG_INFO + "Initiating Node")
        rospy.init_node("cam incoming node")

        self.bridge = CvBridge()
        self.counter = 0

        self.image_msg = rospy.Subscriber("/angela/cameras/main/capture", Image, self.SaveImage)
        # stops the node from exiting
        rospy.spin()
        

    def SaveImage(self, data):
        if self._DEBUG:
            rospy.loginfo(self._DEBUG_INFO + "Saving Image")
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding="rgb8")
        except CvBridgeError as e:
            rospy.logerr(self._DEBUG_INFO)
            rospy.logerr(e)
            return

        savePath = os.path.join('/home/pi/tanis/Images/', (str(self.counter) + '.jpg'))
        # savePath = "/images/" + (str(self.counter) + '.jpg')
        # (filepath, filename) = os.path.split(savePath)
        # print(filepath)
        # print(filename)

        cv2.imwrite(savePath, cv_image)
        if self._DEBUG:
            rospy.loginfo(self._DEBUG_INFO + "Image Saved")
        self.counter += 1

if __name__ == '__main__':
    CamIncoming()
