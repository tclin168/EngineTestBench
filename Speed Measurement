%Program for calculating the speed

import RPi.GPIO as GPIO
import time
from time import sleep

sensor1 = 6
sensor2 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor1, GPIO.IN)
GPIO.setup(sensor2, GPIO.IN)

sample = 4
count = 0

start = 0
end = 0

def set_start():
    global start
    start = time.time()

def set_end():
    global end
    end = time.time()
    
def get_rpm():
    global count
    if count == 0:
        set_start()
        count = count +1
        
    else:
        count = count + 1
    
    if count == sample + 1:
        set_end()
        delta1 = end - start
        rpm2 = 60 / delta1
        print("Motor Speed: "+ {:.2f}".format(str(rpm2)) + " rpm"  +  \ 
        "; Time for on rotation: " + "{:.2f}".format(str(delta)))
        count = 0
        

GPIO.add_event_detect(sensor1, GPIO.RISING, callback = get_rpm) 
#GPIO.add_event_detect(sensor1, GPIO.RISING, callback = get_rpm, bouncetime = 100)

try:
    while True:
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
