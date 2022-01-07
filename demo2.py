#from bluetooth import BTLEDevice
import bluetooth
import time
import logging

logging.basicConfig()
logging.getLogger('bluetooth').setLevel(logging.DEBUG)
# Replace this mac address with the one
# belonging to your train
chief = bluetooth.BTLEDevice("44:A6:E5:48:7F:73")
# chief.set_bell_pitch(1)
chief.connect()
# Gracefully start or stop
def ramp(start_speed, end_speed):
    speed = start_speed
    while speed != end_speed:
        chief.set_speed(speed)
        if speed > end_speed:
            speed -= 1
        else:
            speed += 1
        time.sleep(.2)
    chief.set_speed(end_speed)

while True:
    # Let the conductor say something
    # chief.speak()
    # # Have to give adequate to speak, otherwise horn
    # # will cut off the conductor's voice
    time.sleep(1)

    # # Time to go
 #   chief.set_horn(True)

  #  time.sleep(1)
  #  chief.set_horn(False)




    # # Turn the horn off
   # time.sleep(2)


    chief.set_reverse(False)

    chief.ramp(0,11)

   # time.sleep(2)

#    chief.set_horn(True)

  #  time.sleep(.05)
    # ramp(0, 6)
  #  chief.set_horn(False)
    # chief.set_horn(False)

    # # Keep training along
    time.sleep(10)

    chief.ramp(9,0)

    # # Reverse 
    # ramp(6,0)
    # chief.set_reverse(True)
    # time.sleep(1)
    # ramp(0,6)
    # time.sleep(10)

    # # Back to normal
    # ramp(6,0)
    # chief.set_reverse(False)
    # ramp(0,6)
    # time.sleep(40)

    # # This is our stop
    # chief.set_bell(True)
    # time.sleep(1)
    # ramp(6,0)
    # time.sleep(1)
    # chief.set_bell(False)
    time.sleep(180)

