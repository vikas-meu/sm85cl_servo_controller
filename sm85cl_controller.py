#!/usr/bin/env python

import time
import pyautogui
from scservo_sdk import *

 
PORT = 'COM11'
BAUD = 115200
ID = 1

MAX_SPEED = 0
MAX_ACCEL = 0
 
screen_w, screen_h = pyautogui.size()

 
portHandler = PortHandler(PORT)
packetHandler = sms_sts(portHandler)

if not portHandler.openPort():
    print("Failed to open port")
    quit()
if not portHandler.setBaudRate(BAUD):
    print("Failed to set baudrate")
    quit()

print("Touch screen to control servo 0° → 180°")

try:
    while True:
        x, y = pyautogui.position()

         
        angle = (x / screen_w) * 180.0

       
        pos = int((angle / 360.0) * 4095)

        
        packetHandler.WritePosEx(ID, pos, MAX_SPEED, MAX_ACCEL)

        time.sleep(0.02)   

except KeyboardInterrupt:
    print("Exiting...")
    portHandler.closePort()
