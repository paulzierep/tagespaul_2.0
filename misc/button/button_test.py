import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

#GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use BCM pin numbering
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 26 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 26 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 26 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 26 to be an input pin and set initial value to be pulled low (off)


while True: # Run forever
	if GPIO.input(26) == GPIO.HIGH:
		print("Button 26 was pushed!")
		time.sleep(0.2)
	if GPIO.input(19) == GPIO.HIGH:
		print("Button 19 was pushed!")
		time.sleep(0.2)
	if GPIO.input(13) == GPIO.HIGH:
		print("Button 19 was pushed!")
		time.sleep(0.2)
	if GPIO.input(6) == GPIO.HIGH:
		print("Button 19 was pushed!")
		time.sleep(0.2)
