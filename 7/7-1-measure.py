import RPi.GPIO as GPIO
#from time import sleep 
#from time import time
import time

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
troyka = 17
comp = 4

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 0)
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
#def adc():
#    voltage = 8*[0]
#    
#    gpio.output(dac, 0)
#
#    sleep(0.01)
#
#    for st in range(0, 8):
#        voltage[st] = 1
#
#        gpio.output(dac[st], voltage[st])
#
#        sleep(0.01)
#
#        if (gpio.input(comp) == 0): # led is on
#            voltage[st] = 0
#            gpio.output(dac[st], voltage[st])
#
#    dec = bin_to_dec(voltage)
#    return dec

value = []
start_time = 0
stop_time  = 0
dec = 0

try:
    start_time = time.time()
    GPIO.output(troyka, 1)

    while (dec < 0.95 * 255):
        
        dec = adc()
        print("voltage = {:.3} V, bin = {}".format(dec/255*3.3, dec))
        GPIO.output(leds, decimal2binary(dec))
        value.append(dec/255*3.3)

    GPIO.output(troyka, 0)

    print("Power off")
    while (dec > 0.02 * 255):

        dec = adc()
        print("voltage = {:.3} v, bin = {}".format(dec/255*3.3, dec))
        GPIO.output(leds, decimal2binary(dec))  
        value.append(dec/255*3.3)

    stop_time = time.time()

    with open('measureData.txt', 'w') as f:
        f.write('\n'.join([str(val) for val in value]))

    elapsed_time = stop_time - start_time

    with open('settings.txt', 'w') as f:
        f.write('Время измерения, с\n{:.6f}\n'.format(elapsed_time))
        f.write('Шаг квантования, В\n{:.6f}\n'.format(3.3 / 255))

    print(elapsed_time)
    print('Время измерения, с', elapsed_time)
    print('Период измерения, с', elapsed_time /  len(value))
    print('Частота дискр, Гц', len(value) / elapsed_time)
    print('Шаг квантования, В', 3.3 / 255)
    
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
