#!/usr/bin/env python
'''
**********************************************************************
* Filename    : TB6612.py
* Description : A driver module for TB6612
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-23    New release
**********************************************************************
'''

import picamera
import time
import cv2
import io
import numpy as np


class Camera():

    def __init__(self):        
        self.camera = picamera.PiCamera()
        
    def Capture(self):
        stream = io.BytesIO()

        with self.camera:
            self.camera.start_preview()
            time.sleep(2)
            with self.camera.array.PiRGBArray(self.camera) as stream:
                self.camera.capture(stream, format='rgb')
                image = stream.array
        path = './tanis/Codebase/ros/src/angela/scripts/hardwarein/images'
        cv2.imwrite(os.path.join(path, image))


if __name__ == '__main__':
    Capture()
