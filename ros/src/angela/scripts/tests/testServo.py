#!/usr/bin/env python
import steer
import sys
import time
import RPi.GPIO as GPIO


class Test(object):
    _MIN_PULSE_WIDTH = 600
    _MAX_PULSE_WIDTH = 2400
    _DEFAULT_PULSE_WIDTH = 1500
    _frequency = 60

    def __init__(self):        
        self.angle = int(float(sys.argv[1]))
        print("args loaded")
        self.main()
        
    

    def main(self):
        print("begin steering")
        steering = steer.Steer()

        steering.turn(self.angle)

          
   
if __name__ == '__main__':
    Test()