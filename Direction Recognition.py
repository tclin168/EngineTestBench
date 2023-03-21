%Program for detect t{python}

import RPi.GPIO as GPIO
import time
from time import sleep

sensor1 = 6
sensor2 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor1, GPIO.IN)
GPIO.setup(sensor2, GPIO.IN)

counter = 0
direction = 0
sensor1LastState = GPIO.input(sensor1)

def get_direction():
    global counter
    global direction
    global sensor1State
    global sensor2State
    global sensor1LastState
    try:
        while counter in range (-30, 30):
            sensor1State = GPIO.input(sensor1)
            sensor2State = GPIO.input(sensor2)
            if sensor1State != sensor1LastState:
                if sensor2State != sensor1State:
                    counter += 1 #Left
                    if counter == 25:
                        direction = 'Left'
                        counter = 0
                
                else:
                    counter -= 1 #Right
                    if counter == -25:
                        direction = 'Right'
                        counter = 0
                
                print("Motor Direction: " + str(direction) + " ; Counter: " + str(counter))
            sensor1LastState = sensor1State
            time.sleep(0.0001)
    except KeyboardInterrup:
        print("Quit")
        GPIO.cleanup()

get_direction()he direction.
