import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GP.setup(dac, GP.OUT)
comp = 4
troyka = 17
GP.setup(troyka, GP.OUT, initial = GP.HIGH)
GP.setup(comp, GP.IN)

def dec2bin(value):
    return[int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for value in range(256):
        GP.output(dac, dec2bin(value))
        c = GP.input(comp)
        time.sleep(0.05)
        if c == 0:
            return value


try:
    while True:
        i = adc()
        if i != 0:
            print(i, '{:.2f}v'.format(3.3*i/256))
finally:
    GP.output(dac, 0)
    GP.output(troyka, 0)
    GP.cleanup()