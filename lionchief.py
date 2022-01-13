from contextlib import nullcontext
import bluetooth
import time
import threading

# UUID25 = "08590f7e-db05-467e-8757-72f6faeb13d4"


class LionChief(object):
    

    def __init__(self, mac_address):
        if not mac_address:
            raise "LionChief constructor needs mac address"
        
        self._mac_address = mac_address
        self._blue_connection = None

    def connect(self):
        self._blue_connection=bluetooth.BTLEDevice(self._mac_address)
        self._blue_connection.connect()

    def set_horn(self, on):
        self._send_cmd([0x48, 1 if on else 0])

    def _set_speed(self, speed):
        self._send_cmd([0x45, speed])

    def ramp(self,start_speed,end_speed):
        x=threading.Thread(target=self.ramp_thread,args=(start_speed,end_speed))
        x.start()

    def ramp_thread(self, start_speed, end_speed):
        speed = start_speed
        while speed != end_speed:
            self._set_speed(speed)
            if speed > end_speed:
                speed -= 1
            else:
                speed += 1
            time.sleep(.2)
        self._set_speed(end_speed)

    #zero is random
    def speak(self, phrase=0):
        self._send_cmd([0x4d, phrase, 0])    

    def bell(self, on):
        self._send_cmd([0x47, 1 if on else 0])

    def set_reverse(self, on):
        self._send_cmd([0x46, 0x02 if on else 0x01])   

    def _send_cmd(self, values):
        checksum = 256
        for v in values:
            checksum -= v;
        while checksum<0:
            checksum+=256
        values.insert(0,0)
        values.append(checksum)
        self._blue_connection.char_write(0x25, bytes(values), True)
        # self._device.char_write(25, bytes(values), TRUE);

    def set_over_volume(self, volumn):
        self._send_cmd([0x4c,volumn])

    def set_bell_volume(self, volumn):
        self._send_cmd([0x44,0x02,volumn])

    def set_horn_volume(self, volumn):
        self._send_cmd([0x44,0x01,volumn])

    def set_speech_volume(self, volumn):
        self._send_cmd([0x44,0x03,volumn])

    def set_engine_volume(self, volumn):
        self._send_cmd([0x44,0x04,volumn])
    
    # def set_horn_pitch(self,pitch):
    #     self._send_cmd([0x44,0x01,0x0e,pitch])

    # def set_bell_pitch(self, pitch):
    #     self._send_cmd([0x44,0x02,0x0e,pitch])

    def set_bell_pitch(self, pitch):
        pitches = [0xfe, 0xff, 0, 1, 2]
        if pitch<0 or pitch >=len(pitches):
            print("Bell pitch should be between 0 and "+ str(pitch))
            return
        self._send_cmd([0x44, 0x02, 0x0e, pitches[pitch]])

    def set_horn_pitch(self, pitch):
        pitches = [0xfe, 0xff, 0, 1, 2]
        if pitch<0 or pitch >=len(pitches):
            print("horn pitch should be between 0 and "+ str(pitch))
            return
        self._send_cmd([0x44, 0x01, 0x0e, pitches[pitch]])

    def quit(self):
        self._blue_connection.stop()


    #     self._adapter = pygatt.GATTToolBackend()
    #     self._adapter.start();
    #     self._device = self._adapter.connect(mac);

    # def _send_cmd(self, values):
    #     checksum = 256
    #     for v in values:
    #         checksum -= v;
    #     while checksum<0:
    #         checksum+=256
    #     values.insert(0,0)
    #     values.append(checksum)
    #     self._device.char_write(UUID25, bytes(values));

    # def set_horn(self, on):
    #     self._send_cmd([0x48, 1 if on else 0])

    # def set_bell(self, on):
    #     self._send_cmd([0x47, 1 if on else 0])

    # def set_bell_pitch(self, pitch):
    #     pitches = [0xfe, 0xff, 0, 1, 2]
    #     if pitch<0 or pitch >=len(pitches):
    #         raise "Bell pitch should be between 0 and "+pitch
    #     self._send_cmd([0x44, 0x02, 0x0e, pitches[pitch]]);

    # def speak(self):
    #     self._send_cmd([0x4d, 0, 0])

    # def set_speed(self, speed):
    #     self._send_cmd([0x45, speed])

    # def set_reverse(self, on):
    #     self._send_cmd([0x46, 0x02 if on else 0x01])

    def __del__(self):
        self._blue_connection.stop()
        # if self._adapter:
        #     self._adapter.stop();

