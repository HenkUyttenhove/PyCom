# boot.py -- run on boot-up
import os
import machine
uart = UART(0, 115200)
os.dupterm(uart)

from network import WLAN
wlan = WLAN() # get current object, without changing the mode

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('kawanda.be', auth=(WLAN.WPA2, 'xxxxx'), timeout=5000)
    while not wlan.isconnected():
        machine.idle() # save power while waiting
