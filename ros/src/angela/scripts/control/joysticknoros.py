#!/usr/bin/env python

'''
**********************************************************************
* Filename    : joystickNoROS.py
* Description : Used to test JoyStick
* Author      : Joe Kocsis
* E-mail      : Joe.Kocsis3@gmail.com
* Website     : www.github.com/jkocsis3/tanis
**********************************************************************
'''


from evdev import InputDevice, categorize, ecodes

class JoyStickNoROS(object):
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "JoyStick.py":'

    def __init__(self, debug=True):
        self.DEBUG = debug
        
        self.speed = 0  
        self.turningValue = 90  
        self.controller = InputDevice('/dev/input/event0')
        self.ReadInputs()

    def ReadInputs(self):
        for event in self.controller.read_loop():
            try:            
                if event.type == ecodes.EV_ABS:
                    absevent = categorize(event)
                    # if self._DEBUG:
                    if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RZ':
                        self.speed = absevent.event.value / 10.23
                        if self.speed < 0:
                            self.speed = 0
                        if self.speed > 100:
                            self.speed = 100
                        print(self._DEBUG_INFO + " Speed value = " + str(abs(int(self.speed))))

                    if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_X':                    
                        self.turningValue = 90 + int(absevent.event.value / 1050) 
                        if self._DEBUG:
                            print(self._DEBUG_INFO + "Value from controller: " + str(absevent.event.value))
                            print(self._DEBUG_INFO + " turning value = " + str(int(self.turningValue)))
                         
            except IOError:
                pass
            
if __name__ == '__main__':
    JoyStickNoROS()
