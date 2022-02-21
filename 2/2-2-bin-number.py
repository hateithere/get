#!/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 1]

GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, 0)

#GPIO.output(dac, number)

#time.sleep(15)

nums = [
        [1, 1, 1, 1, 1, 1, 1, 1], #255
        [0, 1, 1, 1, 1, 1, 1, 1], #127
        [0, 1, 0, 0, 0, 0, 0, 0], #64
        [0, 0, 1, 0, 0, 0, 0, 0], #32
        [0, 0, 0, 0, 0, 1, 0, 1], #5
        [0, 0, 0, 0, 0, 0, 0, 0], #0
]

for num in nums:
    print(num)
    GPIO.output(dac, num)
    time.sleep(20)
    GPIO.output(dac, 0)

GPIO.output(dac, 0)

GPIO.cleanup()
