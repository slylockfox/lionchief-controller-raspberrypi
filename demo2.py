

import lionchief
import time
import datetime
import logging
import sys

#This demo class will be split into a common service soon.  This will soon be commandline only interface.

logging.basicConfig()
logging.getLogger('bluetooth').setLevel(logging.DEBUG)
# Replace this mac address with the one
# belonging to your train
#chief = lionchief.LionChief("44:A6:E5:48:7F:73") #steam engine
#chief = bluetooth.BTLEDevice("44:A6:E5:35:54:88") #GE
chief = lionchief.LionChief("D0:EC:B7:01:5E:DE") #steam engine

# chief.set_bell_pitch(1)
try:
    chief.connect()
except Exception as e:
    print(e)
    sys.exit(0)
# Gracefully start or stop
speed=0
reverse = False

def eSpeed(newSpeed,eBrake = False):
    global speed
    if(eBrake == False):
        chief.ramp(speed,newSpeed)
        speed = newSpeed
    else:
        chief._set_speed(0)
        speed = 0

def connectNotify():
    chief.set_horn(True)
    time.sleep(.1)
    chief.set_horn(False)
    time.sleep(.1)
    chief.set_horn(True)
    time.sleep(.1)
    chief.set_horn(False)

def sleepUntilTopOfHour():
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, t.day, (t.hour+1)%24, 0)
    if t.timestamp() > future.timestamp():
        future += datetime.timedelta(days=1)
    time.sleep((future-t).total_seconds())

#chief.set_engine_volume(8)
#chief.bell(True)
#time.sleep(2)
#chief.bell(False)
#time.sleep(10)
#chief.set_engine_volume(0)
while True:
    chief.set_engine_volume(8)
    chief.bell(True)
    time.sleep(2)
    chief.bell(False)
    time.sleep(10)
    chief.set_engine_volume(0)
    #sleepUntilTopOfHour()
    time.sleep(60*60)

while True:

    command = input("Enter your command ")
    if(command == 'q'):
        chief.quit()
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


    if(command == 'bp'):
        bpcommand=input("enter bell pitch")
        chief.set_bell_pitch(int(bpcommand))
        chief.bell(True)
        time.sleep(2)
        chief.bell(False)
    
    if(command == 'hp'):
        print("horn pitch 0,1,2,3,4")
        print("2 is default")
        hpcommand=input("enter HORN pitch ")
        chief.set_horn_pitch(int(hpcommand))
        chief.set_horn(True)
        time.sleep(2)
        chief.set_horn(False)

    if(command == 't'):
        chief.set_horn_pitch(2)
        chief.set_horn(True)
        time.sleep(.7)
        chief.set_horn_pitch(3)
        time.sleep(.03)
        chief.set_horn_pitch(4)
        time.sleep(2)
        chief.set_horn(False)

    if(command == 'eb'):
        eSpeed(0, True)

    if(command == 'ss'):
        sscommand=input("enter a speed: ")
        eSpeed(int(sscommand))

    if(command == 'cd'):
        if(reverse):
            reverse = False
        else:
            reverse = True
        chief.set_reverse(reverse)
        eSpeed(speed)


