#!/usr/bin/env python
import motormove
import sys
import time


class Test(object):
    def __init__(self):
        self.rate = int(float(sys.argv[1]))
        self.direction = int(float(sys.argv[2]))
        self.time = int(float(sys.argv[3]))
        print("args loaded")
        self.main()

    def main(self):
        print("begin movement")
        movement = motormove.MotorMove()
        movement.move(rate=self.rate, direction=self.direction)
        time.sleep(self.time)
        print("stopping motors")
        movement.move(rate=0, direction=0)
        movement.stop()

if __name__ == '__main__':
    Test()
