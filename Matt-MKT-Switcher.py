import lionchief
import time
import datetime
import logging
import sys
import threading
import os

#This demo class will be split into a common service soon.  This will soon be commandline only interface.

logging.basicConfig()
logging.getLogger('bluetooth').setLevel(logging.DEBUG)
# Replace this mac address with the one
# belonging to your train
# chief = lionchief.LionChief("44:A6:E5:48:7F:73") #steam engine
# chief = bluetooth.BTLEDevice("44:A6:E5:35:54:88") #GE
# chief = lionchief.LionChief("D0:EC:B7:01:5E:DE") # Marie steam engine
chief = lionchief.LionChief("18:45:16:98:66:C8") # Matt MKT switcher engine


def watchdog():
    global lion_working
    time.sleep(60)
    if not lion_working:
        os.system('sudo reboot')
    print ("Watchdog ending...", flush=True)

lion_working = False
try:
    print ("Starting watchdog...", flush=True)
    dog_thread = threading.Thread(target = watchdog)
    dog_thread.start()
    chief.connect()
except Exception as e:
    print(e)
    os.system('sudo reboot')
    
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

def sleepUntilTopOfHour():
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, t.day, (t.hour+1)%24, 0)
    if t.timestamp() > future.timestamp():
        future += datetime.timedelta(days=1)
    time.sleep((future-t).total_seconds())

chief.set_bell_pitch(1)

for i in range(1,3):
    try:
      print ("Awake...", flush=True)
      chief.set_engine_volume(8)
      chief.bell(True)
      time.sleep(2)
      chief.bell(False)
      time.sleep(10)
      chief.set_engine_volume(0)
      time.sleep(10)
      chief.set_engine_volume(0)
      chief.set_reverse(True)
      lion_working = True
    except:
      os.system('sudo reboot')
    print ("Sleeping...", flush=True)
    sleepUntilTopOfHour()

chief.set_reverse(False)

