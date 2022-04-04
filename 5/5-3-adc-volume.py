#!/bin/python3

import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setwarnings(False)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def binary2decimal(value):
    res = 0
    for i in range(8):
        res += value[7 - i]* 2**i
    return res

def adc_simple():
    res = [0 for i in range(8)]

    for i in range(8):
        res[i] = 1
        GPIO.output(dac, res)
        time.sleep(0.01)
        value = GPIO.input(4)
        if not value:
            res[i] = 0
    return binary2decimal(res)

def adc_sar():
    for i in range(256):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.01)
        value = GPIO.input(4)
        if not value:
            break
    return i

def one_fill(value):
    print("nya", value)
    pos = 7
    
    for i in range(8):
        if value[i] == 1:
            pos = i
            break
    print("pos:", pos)
    for i in range(7, pos, -1):
        value[i] = 1
    print(value)
    return value

def fill(value):
    res = decimal2binary(0)
    meow = 0
    delta = 256/8
    for i in range(8):
        if value >= meow:
            res[7 - i] = 1
            meow += delta
        else:
            break
    #print(res)
    return res

try:
    while (True):
        value = adc_sar()
        GPIO.output(leds, fill(value))

except KeyboardInterrupt:
    print("Finished")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
