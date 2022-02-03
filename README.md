# LOTS OF TODO.  This looks a bit confusing, but this will be cleaned up and broken into a service that command line will work with and a WEB api.
### todo singletons
### todo web authentication using Microsoft Account

# LionChief Controller
Script for controlling a LionChief train via Bluetooth

## About
LionChief trains can be controlled via Bluetooth(BLE, not classic) from a smart phone
using the LionChief app.  

Android has a bluetooth snooping feature. Using this with Wireshark, I was able
to figure out which GATT/ATT handle and value pairs to use to change speed, 
make noise, and more.  

This is adapted from Property404's code but changed quite a bit.  This no longer uses Pygatt but only wrapps gatttools.

This has the bassic commands, but I do plan on adding changing the volume commands in the future too.

All basic commands use handle 0x25 (UUID 08590f7e-db05-467e-8757-72f6faeb13d4).
Each command starts with 0x00, and ends with a checksum. Interestingly, the
train doesn't seem to actually -check- the checksum, but it's possibly logged
somewhere? I included the checksum calculation in the `LionChief` class, anyway.  

### Commands (excluding checksum and leading zero)
Horn start: `48 01`  
Horn stop : `48 00`  
Bell start: `47 01`  
Bell stop : `47 00`  
Speech    : `4d XX 00`  
Set speed : `45 <00-1f>`  
Forward   : `46 01`  
Reverse   : `46 02`  
Overall Volume: `4C XX`  0-7  
engine volumn: `44 04 XX` 0-15  
horn volumn:  `44 01 XX`  
bell volumn: `44 02 XX`    
speach volumn: `44 03 XX` 

bell pitch: `44 01 0e XX`  
-2,-1,0,1,2 NOTE Negative hex values are:

horn pitch: `44 02 0e XX`  
-2,-1,0,1,2 NOTE Negative hex values are:

If the first parameter of the speech command is 0, the saying will be random.
Otherwise, each value corresponds to a specific saying. Not sure what the
second parameter does.

1225 Speech codes (Polar Express)
1 - this is the poloar express
2 - all aboard
3 - well you coming
4 - tickets.  #tickets please
5 - The first gift of christmas
6 - I am the king of the north pole

## Usage
Demo usage can be found in `demo2.py`. Make sure to change the MAC address
(how to get MAC Address...more to come on that)

## Requirements
Tested with Python 3.9. Not expected to work outside Linux  
`pygatt`  
`pybluez`
`pexpect`

## Helpful Links for Future Projects
[The Practical Guide to Hacking BLE](https://blog.attify.com/the-practical-guide-to-hacking-bluetooth-low-energy/)  
[How to sniff Bluetooth traffic on Andorid](https://stackoverflow.com/questions/23877761/sniffing-logging-your-own-android-bluetooth-traffic)  
[About ATT and GATT](https://epxx.co/artigos/bluetooth_gatt.html)

## License
MIT
