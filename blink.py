#!/usr/bin/env python2.7
import RPi.GPIO as GPIO
from time import sleep

pin = 18
pause_time = 0.02

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

# put the main part of your code inside a try block
try:
    while True:
	    GPIO.output(pin, True)
	    sleep(pause_time)
	    GPIO.output(pin, False)
	    sleep(pause_time)

# this code executes any time that a KeyboardInterrupt exception occurs
# this happens when you press Ctrl + C
except KeyboardInterrupt:
	GPIO.cleanup()
