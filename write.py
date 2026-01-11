#!/usr/bin/env python

#
# Move SM85CL from 180° to 0° at max speed
#

import time
from scservo_sdk import *

PORT = 'COM11'
BAUD = 115200        # default baud for SMS series

ID = 1

# position mapping
POS_0   = 0
POS_180 = 2047       # half of 4095

# max speed / accel
MAX_SPEED = 0        # 0 = fastest (SMS protocol)
MAX_ACCEL = 0        # 0 = fastest

portHandler = PortHandler(PORT)
packetHandler = sms_sts(portHandler)

# open port
if not portHandler.openPort():
    print("Failed to open port")
    quit()
print("Port opened")

if not portHandler.setBaudRate(BAUD):
    print("Failed to set baudrate")
    quit()
print("Baudrate set")

print("Starting fastest 180 ↔ 0 motion...")

while True:
    # move to 180 degrees
    packetHandler.WritePosEx(ID, POS_180, MAX_SPEED, MAX_ACCEL)
    time.sleep(0.4)   # allow time to reach (tune for your servo)

    # move back to 0 degrees
    packetHandler.WritePosEx(ID, POS_0, MAX_SPEED, MAX_ACCEL)
    time.sleep(0.4)   # tune if needed
