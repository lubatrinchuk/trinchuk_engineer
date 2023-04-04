import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GP.setup(dac, GP.OUT)

def dec2bin(value):
    return[int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    print("Период:")
    n = int(input())
    while True:
        for i in range(256):
            b = []
            b = dec2bin(i)
            GP.output(dac, b)
            time.sleep(n/512)
        for i in range(255, -1, -1):
            b = []
            b = dec2bin(i)
            GP.output(dac, b)
            time.sleep(n / 512)
finally:
    GP.output(leds, 0)
    GP.cleanup()