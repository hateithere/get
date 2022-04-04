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

def binary2decimal(value):
    res = 0
    for i in range(8):
        res += value[7 - i]* 2**i
    return res

def adc():
    res = [0 for i in range(8)]

    for i in range(8):
        res[i] = 1
        GPIO.output(dac, res)
        time.sleep(0.01)
        value = GPIO.input(4)
        if not value:
            res[i] = 0
    return binary2decimal(res)
    #return res

try:
    while (True):
        start = datetime.now()
        value = adc()
        print("time:", datetime.now() - start)
        print("value: {:d}, voltage: {:.4f}".format(value, 3.3/2**8*value))

        #print(value)

except KeyboardInterrupt:
    print("Finished")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
