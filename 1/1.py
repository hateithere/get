#!/bin/python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

GPIO.output(14, 1)
sleep(2)
GPIO.output(14, 0)
sleep(2)
GPIO.output(14, 1)
sleep(2)
GPIO.output(14, 0)
