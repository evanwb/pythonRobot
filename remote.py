from gpiozero import Robot, DistanceSensor
import blynklib
#import video

lfPin = 24
lbPin = 23
rfPin = 21
rbPin = 25


robot = Robot(left=(lfPin,lbPin), right=(rfPin,rbPin))
sensor = DistanceSensor(14, 15, max_distance=1, threshold_distance=0.2)

BLYNK_AUTH = '30uy6Ic_5neoK6wUOjXhEm91-l6epS_C'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH, server='127.0.0.1', port=8080, ssl_cert=None, log=print)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"


# register handler for virtual pin V4 write event
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    x=int(value[0]) 
    y=int(value[1])
    if x<50:
      robot.left()
    elif x>220:
      robot.right()
    elif y<30:
      robot.backward()
    elif y>180:
      robot.forward()
    else:
      robot.stop() 
    read_virtual_pi_handler(pin)  

@blynk.handle_event('read V2')
def read_virtual_pin_handler(pin):
   if sensor.distance*100<80:                                                                            │# register handler for virtual pin V4 write event
   #while sensor.distance*100<70:                                                                       │@blynk.handle_event('write V4')
     print('backward')                                                                                  │def write_virtual_pin_handler(pin, value):
     #robot.backward()                                                                                  │    x=int(value[0]) 
     robot.stop                                                                                         │    y=int(value[1])
     robot.backward()                                                                                   │    if x<50:
     robot.left()                                                                                       │      robot.left()
                                                                                                        │    elif x>220:
   else:                                                                                                 │      robot.right()
     print('forward')                                                                                     │    elif y<30:
     #print(sensor.distance*100)                                                                          │      robot.backward()
     robot.forward()   


@blynk.handle_event('read V1')
def read_virtual_pin_handler(pin):
    print(sensor.distance*100) 
    blynk.virtual_write(pin, (sensor.distance*100))    


###########################################################
# infinite loop that waits for event
###########################################################

while True:
    blynk.run()
 #   print(sensor.distance)
