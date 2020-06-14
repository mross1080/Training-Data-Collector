# TINYML Training Data Collector

This Library is meant to serve as the server to collect training data from the Arduino BLE Sense 33 for training.  Though it would work with any Serial Connected microcontroller.

This process will help if you are following the instructions from this tutorial.  
https://blog.arduino.cc/2019/10/15/get-started-with-machine-learning-on-arduino/

#### Installation

`pip install pyserial`


#### Arduino Instructions

Upload this file onto your arduino ble sense 33

https://raw.githubusercontent.com/arduino/ArduinoTensorFlowLiteTutorials/master/GestureToEmoji/ArduinoSketches/IMU_Capture/IMU_Capture.ino

#### Run Instructions
Open the terminal into this directory and then run

`python collect_arduino_data.py`

The program will ask you to name the file you would like to output your data to.  Make sure you give the file in quotation marks.  The name doesn't really matter, whatever makes you happy.
