import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 8, 5, 18, 17]
GP.setup(dac, GP.OUT)
comp = 4
troyka = 17
GP.setup(troyka, GP.OUT, initial=GP.HIGH)
GP.setup(comp, GP.IN)
GP.setup(leds, GP.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():
    value = 0
    for bit in range(7, -1, -1):
        value += 2**8
        GP.output(dac, dec2bin(value))
        time.sleep(0.05)
        if GP.input(comp) == 0:
            value -= 2**8
    return value


try:
    while True:
        i = adc()
        GP.output(leds, dec2bin(i))
        if i != 0:
            print(i, '{:.2f}v'.format(3.3 * i / 256))
finally:
    GP.output(dac, 0)
    GP.output(troyka, 0)
    GP.cleanup()