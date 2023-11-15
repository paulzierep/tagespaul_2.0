#basic modules
import time
import random
import subprocess
import os
import signal

# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO 

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

###########################
#LEDs
###########################

# Configure the count of pixels:
PIXEL_COUNT = 15
 
# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

###########################
#Buttons
###########################

#GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use BCM pin numbering
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 26 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 26 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 26 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 26 to be an input pin and set initial value to be pulled low (off)


def 


###########################
#Colors
###########################

j = 0
while True: # Run forever

    set_rainbow_colors_offset(pixels,j)
    j += 1

    if GPIO.input(26) == GPIO.HIGH: