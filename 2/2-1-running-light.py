#!/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

for j in range(3):
    for i in range(len(leds)):
        if i != 0: 
            GPIO.output(leds[i-1], 0)
            GPIO.output(leds[i], 1)
        else:
           GPIO.output(leds[i], 1)
           GPIO.output(leds[-1], 0)
        time.sleep(0.2)

GPIO.output(leds, 0)

GPIO.cleanup()
