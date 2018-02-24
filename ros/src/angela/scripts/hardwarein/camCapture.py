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
from picamera.array import PiRGBArray


class Camera():
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "camCapture.py2":'

    def __init__(self, debug=False):
        self._DEBUG = debug
        rospy.init_node('Camera_Cap_Node')
        rospy.loginfo(self._DEBUG_INFO + " initializing node")

        
        self.image_pub = rospy.Publisher("/angela/cameras/main/capture", Image, queue_size=10)
        
        self.rate = rospy.Rate(10)
        self.camera = picamera.PiCamera()
        while not rospy.is_shutdown():
            self.CaptureVideo()            
            # self.rate.sleep()
        self.camera.close()

    def CaptureStill(self):        
        
        rawCapture = PiRGBArray(self.camera)
        self.camera.start_preview()
        # https://answers.ros.org/question/199294/publish-image-msg/
        self.camera.capture(rawCapture, format='bgr')
        image = rawCapture.array
        msgImage = CvBridge().cv2_to_imgmsg(image, encoding="rgb8")
        self.image_pub.publish(msgImage)

    def CaptureVideo(self):
        self.camera.resolution = (640, 480)
        self.camera.framerate = 32
        rawCapture = PiRGBArray(self.camera, size=(640, 480))
        for frame in self.camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
            msgImage = CvBridge().cv2_to_imgmsg(image, encoding="rgb8")
            self.image_pub.publish(msgImage)
            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)


if __name__ == '__main__':
    Camera()
