from time import sleep
import sys
import os

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

p1 = 14
p2 = 15

GPIO.setup(p1, GPIO.OUT)
GPIO.setup(p2, GPIO.OUT)

class Quit(Exception): pass

def green(duration):
	GPIO.output(p1, False)
	GPIO.output(p2, True)
	sleep(duration)
	GPIO.output(p2, False)

def red(duration):
	GPIO.output(p2, False)
	GPIO.output(p1, True)
	sleep(duration)
	GPIO.output(p1, False)

def main():
	while True:
		# The standard Linux clear screen cmmand.
		n=os.system("clear")
		while True:
			beats=raw_input("Enter any whole number from 30 to 400 (bpm), Q or X to quit. (100): ")
			
			if beats.isdigit():
				if beats <= 400 and beats >= 30:
					break
			
			elif beats.upper() == "Q" or beats.upper() == "X":
				raise Quit
			
			elif beats == "":
				beats = 100
				break
		
		# Now convert to the floating point value for the time.sleep() function.
		beat=((60/float(beats))-0.125)
		
		print("Press Ctrl-C to enter another speed...")
		
		n = 0
		while True:
			try:
				n += 1
				if n < 4:
					green(beat/2)
				
				else:
					n = 0
					red(beat/2)
				
				sleep(beat/2)
			
			except KeyboardInterrupt:
				GPIO.cleanup()
				break

try:
	main()
	GPIO.cleanup()

except Quit:
	GPIO.cleanup()