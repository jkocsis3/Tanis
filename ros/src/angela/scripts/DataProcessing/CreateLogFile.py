#!/usr/bin/env python

'''
**********************************************************************
* Filename    : CreateLogFile.py
* Description : Takes an image from the camera and an angle from the servo
*               and writes them to a CSV file
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
from angela.msg import steermsg


class CreateLogFile(object):
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "CreateLogFile.py":'

    def __init__(self, debug=False):

        self._DEBUG = debug
        rospy.loginfo(self._DEBUG_INFO + "Initiating Node")
        rospy.init_node("Collate_Training_Data")

        self.bridge = CvBridge()
        self.counter = 0
        self.currentImage = 0
        self.currentAngle = 0
        self.savePath = os.path.join('/home/pi/tanis/Images/')

        self.file = open(self.savePath + 'data.csv', 'a')

        self.image_sub = rospy.Subscriber("/angela/cameras/main/capture", Image, self.SetImage)
        self.speed_sub = rospy.Subscriber('/angela/steer/setAngle', steermsg, self.SetAngle)
        # stops the node from exiting
        rospy.spin()

        self.file.close()
        
    # Whenever an image message is recieved, set the incoming image to the current image.
    def SetImage(self, data):
        if self._DEBUG:
            rospy.loginfo("setting image")
        self.currentImage = self.bridge.imgmsg_to_cv2(data, desired_encoding="rgb8")
        self.CollateAndSaveData()

    def SetAngle(self, data):
        if self._DEBUG:
            rospy.loginfo("setting angle")
        self.currentAngle = data.angle   

    def CollateAndSaveData(self):
        if self._DEBUG:
            rospy.loginfo("Saving Data")
        
        cv2.imwrite(self.savePath + (str(self.counter) + '.jpg'), self.currentImage)
        
        self.file.write(str(self.counter) + ', ' + str(self.currentAngle) + '\n')
        
        self.counter += 1

if __name__ == '__main__':
    CreateLogFile()
