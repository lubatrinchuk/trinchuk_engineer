import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 1, 0, 1]
GP.setup(dac, GP.OUT)

GP.output(dac, number)
time.sleep(15)

GP.output(dac, 0)
GP.cleanup()