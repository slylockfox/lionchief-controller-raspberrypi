#from bluetooth import BTLEDevice
import bluetooth
import time
import logging

logging.basicConfig()
logging.getLogger('bluetooth').setLevel(logging.DEBUG)
# Replace this mac address with the one
# belonging to your train
chief = bluetooth.BTLEDevice("44:A6:E5:48:7F:73") #steam engine
#chief = bluetooth.BTLEDevice("44:A6:E5:35:54:88") #GE

# chief.set_bell_pitch(1)
chief.connect()
# Gracefully start or stop
speed=0
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

def connectNotify():
    chief.set_horn(True)
    time.sleep(.1)
    chief.set_horn(False)
    time.sleep(.1)
    chief.set_horn(True)
    time.sleep(.1)
    chief.set_horn(False)

#connectNotify()

while True:


    command = input("Enter your command ")
    if(command == 'q'):
        chief.stop()
        break
    if(command == 'h'):
        chief.set_horn(True)
        time.sleep(1)
        chief.set_horn(False)
    if(command == 'f'):
        if(speed == 0):
            speed = 2
        chief.ramp(speed,speed+1)
        speed+=1
        
        print("Current speed: " , speed)
    if(command == 'b'):
        chief.ramp(speed,0)
        speed=0

    if(command =='v'):
        vcommand=input("enter Volume: ")
        chief.set_over_volume(int(vcommand))
    
    if(command == 'ev'):
        ecommand=input("enter engine Volumne: ")
        chief.set_engine_volume(int(ecommand))

    if(command == 'hv'):
        ecommand=input("enter horn Volumne: ")
        chief.set_horn_volume(int(ecommand))

    if(command == 'sv'):
        ecommand=input("enter speech Volumne: ")
        chief.set_speech_volume(int(ecommand))

    if(command == 'bv'):
        ecommand=input("enter bell Volumne: ")
        chief.set_bell_volume(int(ecommand))

    if(command == 's'):
        chief.speak()

    if(command == 'd'):
        chief.bell(True)
        time.sleep(2)
        chief.bell(False)
    # Let the conductor say something
    # chief.speak()
    # # Have to give adequate to speak, otherwise horn
    # # will cut off the conductor's voice
    # time.sleep(1)

    # # Time to go
 #   chief.set_horn(True)

  #  time.sleep(1)
  #  chief.set_horn(False)




    # # Turn the horn off
   # time.sleep(2)


    #chief.set_reverse(False)

    #chief.ramp(0,11)

    # chief.speak(1) #this is the poloar express

    # time.sleep(2)
    # chief.speak(2) #all aboard
    # time.sleep(2)
    # chief.speak(3) #well you coming
    # time.sleep(2)
    # chief.speak(4) #tickets.  #tickets please
    # time.sleep(2)
    # chief.speak(5) #The first gift of christmas
    # time.sleep(2)
    # chief.speak(6) # I am the king of the north pole
    # time.sleep(2)
   

#    chief.set_horn(True)

  #  time.sleep(.05)
    # ramp(0, 6)
  #  chief.set_horn(False)
    # chief.set_horn(False)

    # # Keep training along
    # time.sleep(10)

    # chief.ramp(0,9)

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
    # time.sleep(180)

