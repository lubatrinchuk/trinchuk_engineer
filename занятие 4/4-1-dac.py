import RPi.GPIO as GP
import sys

GP.setmode(GP.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GP.setup(dac, GP.OUT)

def dec2bin(value):
    return[int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:
        print("enter a number from 0 to 255")
        a = int(input())
        if a == 'q':
            sys.exit()
        elif int(a)%1==0 and 0<=int(a)<=255:
            number = []
            number = dec2bin(a)
            print(number)
            GP.output(dac, number)
            print("{:.4f}".format(int(a)/256*3.3))
        elif not int(a)%1==0:
            print("enter a number from 0 to 255")
except ValueError:
    print("enter a number from 0 to 255")
finally:
    GP.output(leds, 0)
    GP.cleanup()