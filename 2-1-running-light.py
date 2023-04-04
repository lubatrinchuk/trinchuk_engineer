import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
GP.setup(leds, GP.OUT)

a = 0
while a < 3:
    for i in range(8):
        GP.output(leds[i], 1)
        time.sleep(0.2)
        GP.output(leds[i], 0)
    a += 1

GP.output(leds, 0)
GP.cleanup()