#!/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start(0)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while (True):
        dc = input()
        dc = int(dc)
        p.stop()
        p.start(dc)
        print(3.3/100*dc)

except ValueError:
    print("Invalid input")
finally:
    GPIO.cleanup()
