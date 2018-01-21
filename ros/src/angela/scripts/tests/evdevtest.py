#!/usr/bin/env python

from evdev import InputDevice, categorize, ecodes


class ControlTest(object):
    _DEBUG = True
    _DEBUG_INFO = 'DEBUG "speedInput.py2":'

    def __init__(self, debug=True):
        
        self.controller = InputDevice('/dev/input/event0')
        for event in self.controller.read_loop():
            try:            
                if event.type == ecodes.EV_ABS:
                    absevent = categorize(event)
                    print(ecodes.bytype[absevent.event.type][absevent.event.code])
                    # if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_LZ':
                        
            except IOError:
                pass
            

            
if __name__ == '__main__':
    ControlTest()
