from time import sleep
import sys
import os

class Quit(Exception): pass

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
		while True:
			# Write directly to the /dev/dsp device.
			try:
				#audio=open("/dev/dsp", "wb")
				#audio.write(b"\x00\xFF")
				#audio.close()
				sys.stdout.write("\a")     # ASCII bell character
				sleep(beat)
			# There is a flaw here, I'll let you big guns find it... ;o)
			# Note it is NOT really a bug!
			except KeyboardInterrupt: break

try:
	main()
except Quit: x=1