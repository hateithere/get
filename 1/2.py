#!/bin/python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

GPIO.output(14, GPIO.input(15))

