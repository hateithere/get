#!/bin/python3

import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setwarnings(False)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.01)
        value = GPIO.input(4)
        if not value:
            break
    return i

try:
    while (True):
        start = datetime.now()
        value = adc()
        print("time:", datetime.now()-start)
        print("value: {:d}, voltage: {:.4f}".format(value, 3.3/2**8*value))

except KeyboardInterrupt:
    print("Finished")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
