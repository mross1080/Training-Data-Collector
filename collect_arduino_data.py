# -*- coding: utf-8 -*-


import argparse
from time import sleep
import time
from serial import Serial
import os
import serial.tools.list_ports

import subprocess
def init_serial_connection():
     global ser
     port_name = '/dev/cu.usbmodem143111'
     try:
         ports = serial.tools.list_ports.comports()
         for port in ports:
              if "/dev/cu.usbmodem" in port.device:
                   port_name = port.device
                   print("Found an Arduino!! Using {} for specified port\n\n".format(port_name))
         ser = Serial(port_name, 9600)  # Establish the connection on a specific port
         return ser
     except Exception as e:
         print(e)
         print("You've got the Arduino Editor Serial Monitor Open!!! Ya gotta close that puppy!")
         exit()

ser = init_serial_connection()


output_file = input("Hello Friend, I see you are trying to collect some data from a microcontroller.  \nPlease Enter the name of the file you want to create and hit ENTER \n\n")


print("Outputting Data to : " , output_file)
print("\n\n\n\nReady to recieve training data, please start moving the Arduino.  Hit ctrl + c when you are done! ")
termination_status = False
first_line = True
while True:
    try:
      with open('./{}'.format(output_file), 'a') as file_writer:
        if first_line:
            # Write the CSV Param Header
            file_writer.write("aX,aY,aZ,gX,gY,gZ" + os.linesep)
        line = ser.readline().decode().strip(" ").strip("\n")
        file_writer.write(line + os.linesep)
        print(line)


    except Exception as e:
        print(e)
