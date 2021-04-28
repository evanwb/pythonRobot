
from gpiozero import Robot, DistanceSensor
from signal import pause
import time

sensor = DistanceSensor(14, 15, max_distance=1, threshold_distance=0.2)
lfPin = 24
lbPin = 23
rfPin = 21
rbPin = 25
i=0

robot = Robot(left=(lfPin,lbPin), right=(rfPin,rbPin))


#while True:
# print(sensor.distance*100)
# time.sleep(.5)

def auto():
 while True:
  if sensor.distance*100<80:
   #while sensor.distance*100<70:
     print('backward')
     #robot.backward()
     robot.stop
     robot.backward()
     robot.left()
   
  else:
   print('forward')
   #print(sensor.distance*100)
   robot.forward()
 
auto()
