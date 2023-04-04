import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
GP.setup(leds, GP.OUT)
GP.setup(aux, GP.IN)


while True:
    for i in range(8):
        GP.output(leds[i], GP.input(aux[i]))