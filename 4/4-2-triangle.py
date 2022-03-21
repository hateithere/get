#!/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    freq = int(input())
    while (True):
        for i in range(255):
            time.sleep(1/freq)
            GPIO.output(dac, decimal2binary(i))
        for i in range(255, 0, -1):
            time.sleep(1/freq)
            GPIO.output(dac, decimal2binary(i))
        GPIO.output(dac, 0)

except ValueError:
    print("Invalid input")
finally:
    GPIO.output(dac, 0)
