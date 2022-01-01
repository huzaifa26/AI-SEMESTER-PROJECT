#!/usr/bin/env python3
"""Control an Arduino over the USB port."""
# usb.py
# Created by John Woolsey on 12/17/2019.
# Copyright (c) 2019 Woolsey Workshop.  All rights reserved.
# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible

USB_PORT = "/dev/ttyUSB0"

import serial

def print_commands():
   """Prints available commands."""
   print("Available commands:")
   print("  START  ")
   print("  STOP  ")

try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except e:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print(e)
   exit()
# Send commands to Arduino
print("Enter a command from the keyboard to send to the Arduino.")
print_commands()

while True:
    command = input("Enter command: ")
    if command == "START": 
        usb.write(b'START')
        print("STARTING THE CAR")
    elif command == "STOP":
        usb.write(b'STOP')
        print("STOPPING THE CAR")