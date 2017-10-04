#   This code is used to control a Pycom IOT device via html for switching 4 relays on a Keyes Funduino board
#
# Code has been created by Henk Uyttenhove
# Date: 04 Oct 2017
#
# Code is free to use

import socket     # import the IP stack
import time       # import required for delay for dooropener
from machine import Pin    # Control via pins the Keyes Funduino 4-relay board
# addr = socket.getaddrinfo('location.dyndns.org', 80)[0][-1] # only used in case of DNS resolution
p_4 = Pin('P4', mode=Pin.OUT)   # Used for relay 1, on-off
p_8 = Pin('P8', mode=Pin.OUT)   # Used for relay 2, on-off
p_9 = Pin('P9', mode=Pin.OUT)   # Used for relay 3, off-hook the phone
p_10 = Pin('P10', mode=Pin.OUT) # Used for relay 4, after off-hook, open door
addr =('172.16.0.30',80)        # IP address to be used to connect
s = socket.socket()
s.bind(addr)        # bind the board to the IP address
s.listen(1)         # listen to a single session, no multiple connections allowed
while True:
    cl, port = s.accept()   # cl is the IP of connecting client, port is TCP port
    data = cl.recv(10)      # receive 10 bytes
    dataString = data.decode('utf-8')[-5:] #convert the bytes into string and take last 5 char
    if dataString == "D7jzF":      #Set the code to be used in the html call 172.16.0.30/D7jzF
        if p_4():
            p_4(False)
        else:
            p_4(True)
    if dataString == "KxK6c":
        if p_8():
            p_8(False)
        else:
            p_8(True)
    if dataString == "5KhGD":
        p_9(True)
        time.sleep(2)
        p_10(True)
        time.sleep(5)
        p_9(False)
        p_10(False)
    cl.close()
s.close()
