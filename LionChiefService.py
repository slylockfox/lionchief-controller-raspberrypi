import lionchief
import time
import logging
import sys

logging.basicConfig()
logging.getLogger('bluetooth').setLevel(logging.DEBUG)
# Replace this mac address with the one
# belonging to your train
#chief = lionchief.LionChief("44:A6:E5:48:7F:73") #steam engine
chief = lionchief.LionChief("44:A6:E5:35:54:88") #GE

# speed = 0

class LionApi(object):
    # speed = 0
    def __init__(self):
        self.online=True
        self._speed=0
        self._reverse = False

    def start(self):
        try:
            chief.connect()
        except Exception as e:
            print(e)
            sys.exit(0)

    def go(self,newSpeed=0):
        # global speed
        chief.ramp(self._speed, newSpeed)
        self._speed = newSpeed

    def horn(self):
        chief.set_horn(True)
        time.sleep(.5)
        chief.set_horn(False)

    #trying to emulate a twil horn sound for a steam engine.  Can't find a way to make it sound even yet
    def hornTwil(self):
        chief.set_horn_pitch(0)
        chief.set_horn(True)
        time.sleep(.3)
        chief.set_horn_pitch(4)
        time.sleep(2)
        chief.set_horn(False)

    def reverse(self):
        chief.set_reverse(True)
        print('going in reverse')
        self._reverse = True
        self._speed = 0
    
    def forward(self):
        chief.set_reverse(False)
        self._reverse = False
        self._speed = 0