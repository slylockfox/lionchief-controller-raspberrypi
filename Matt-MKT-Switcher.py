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
    time.sleep(300) # 5 minutes
    if not lion_working:
        os.system('sudo reboot')
    print ("Watchdog ending...", flush=True)

def startWatchdog():
    lion_working = False
    try:
        print ("Starting watchdog...", flush=True)
        dog_thread = threading.Thread(target = watchdog)
        dog_thread.start()
    except Exception as e:
        print(e)
        os.system('sudo reboot')
    
# ~ speed=0
# ~ reverse = False

# ~ def eSpeed(newSpeed,eBrake = False):
    # ~ global speed
    # ~ if(eBrake == False):
        # ~ chief.ramp(speed,newSpeed)
        # ~ speed = newSpeed
    # ~ else:
        # ~ chief._set_speed(0)
        # ~ speed = 0

def sleepUntilTopOfHour():
    t = datetime.datetime.today()
    future = datetime.datetime(t.year, t.month, t.day, (t.hour+1)%24, 0)
    if t.timestamp() > future.timestamp():
        future += datetime.timedelta(days=1)
    time.sleep((future-t).total_seconds())

def sleepUntilMinute():
    t = datetime.datetime.today()
    if t.minute == 59:
        future_minute = 0
        if t.hour == 23:
            future_day = t.day + 1
            future_hour = 0
        else:
            future_day = t.day
            future_hour = t.hour+1
    else:
        future_minute = t.minute+1
        future_hour = t.hour
    future = datetime.datetime(t.year, t.month, future_day, future_hour, future_minute)
    if t.timestamp() > future.timestamp():
        future += datetime.timedelta(days=1)
    time.sleep((future-t).total_seconds())

startWatchdog()

try:
    chief.connect()
except Exception as e:
    print(e)
    os.system('sudo reboot')

chief.set_bell_pitch(1)
chief.set_reverse(False)
chief.set_engine_volume(0)

# ring bell
chief.bell(True)
time.sleep(2)
chief.bell(False)

# count = 1
while True:
    try:
        
        print ("Awake...", flush=True)

        # every minute, set reverse, than forward
        chief.set_reverse(True)
        time.sleep(2)
        chief.set_reverse(False)
        time.sleep(2)
        chief.set_reverse(True)
        time.sleep(2)
        chief.set_reverse(False)
        time.sleep(2)

        # every hour, ring bell
        t = datetime.datetime.today()
        if t.minute == 0:
            startWatchdog()
            print ("Sounding bell on the hour...", flush=True)
            chief.bell(True)
            time.sleep(2)
            chief.bell(False)
    
    # ~ if count <= 3:
        # ~ try:
          # ~ print ("Awake...", flush=True)
          # ~ chief.set_engine_volume(8)
          # ~ chief.bell(True)
          # ~ time.sleep(2)
          # ~ chief.bell(False)
          # ~ time.sleep(10)
          # ~ chief.set_engine_volume(0)
          # ~ time.sleep(10)
          # ~ chief.set_engine_volume(0)
          # ~ chief.set_reverse(True)
          # ~ lion_working = True
          # ~ count += 1
          
        lion_working = True
          
    except:
        os.system('sudo reboot')
        
    # ~ else:
        # ~ chief.set_reverse(False) # after 3 hours, put forward headlight back on and be quiet
        
    print ("Sleeping...", flush=True)
    # sleepUntilTopOfHour()
    sleepUntilMinute()



