# Python Remote Control Robot

## Contents
- [Usage](#usage)
- [Camera Feed](#camera-feed)
- [Parts List](#parts-list)
- [Synopsis](#synopsis)

### Usage

```
  pip install -r requirements.txt
  sh bot.sh
```
### Camera Feed

##### To view the feed capture visit this page with the ip address of your device

http://'YOUR DEVICE IP ADDRESS':3030/

### Parts List
 - 3D Printed Chassis
 - Raspberry Pi (Any Model B or B+) 
 - HC-SR04 Ultrasonic Sensor
 - L298N Motor Driver Board
 - 4 x TT Gearbox Motors
 - 4 x Wheels
 - Pi Camera Module
 - Wires to connect components
 

### Synopsis

For my Honors Contract project for the Spring semester, I created an autonomous robot based on a Raspberry Pi. The robot can be operated in two modes. The first is a remote controlled mode, in this mode the robot is controlled by the blynk app. The blynk project consists of an analog joystick directional input, two buttons for mode switching, and a value display to view the distance in centimeters recorded by the ultrasonic sensor. The second mode is autonomus mode, in this mode the robot move forward until the distance sensor records a value less than the provided threshold. Once this occurs the robot will immediately stop, move backwards, turn until the sensor value is above the threshold, then proceed to move forward again. The feed from the Pi Camera is displayed using opencv to capture frames and flask to display them on a webpage. On my Raspberry Pi 4 i was able to get framerate of about 30fps
