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
    while (True):
        value = input()
        if value == 'q':
            break
        value = int(value)
        if (value > 255):
            raise ValueError
        GPIO.output(dac, decimal2binary(value))
        print("voltage: {:.4f}".format(3.3/2**8*value))
except ValueError:
    print("Invalid input")
finally:
    GPIO.output(dac, 0)
