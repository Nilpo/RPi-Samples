#!/usr/bin/env python2.7
import RPi.GPIO as GPIO
from time import sleep

# for safety, lets's be absolutely sure everything is off to begin
GPIO.cleanup()

btn = 25
red = 7
grn = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(grn, GPIO.OUT)

try:
    while True:
        if ( GPIO.input(btn) ):
            # button is pressed, show green
            GPIO.output(red, False)
            GPIO.output(grn, True)
        
        # always turn active pin off before changing states
        GPIO.output(grn, False)
        GPIO.output(red, True)
        
        # prevent button bounce
        sleep(0.05)

# this code executes any time that a KeyboardInterrupt exception occurs
# this happens when you press Ctrl + C
except KeyboardInterrupt:
	GPIO.cleanup()
