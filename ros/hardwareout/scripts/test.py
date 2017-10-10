import raspiinterfaceout
import sys
import time


class Test(object):
	def __init__(self):
		self.rate = int(float(sys.argv[1]))
		self.time = int(float(sys.argv[2]))
		print("args loaded")
		self.main()

	def main(self):
		print("begin movement")
		movement = raspiinterfaceout.MotorMove(rate=self.rate, time=self.time)
		movement.moveForward()
		time.sleep(self.time)
		movement.stop()




if __name__ == '__main__':
	Test()


