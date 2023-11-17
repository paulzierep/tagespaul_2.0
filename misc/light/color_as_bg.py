#basic modules
import time
import random
import subprocess
import os
import signal

import argparse

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

def increase_to_color(pixels, wait=0.002, step = 0.01, color = [0,0,256]):

    for j in range(256):

        rgb = [
        int(color[0] / 256 * j), 
        int(color[1] / 256 * j), 
        int(color[2] / 256 * j)
        ]
        print(rgb)

        for i in range(pixels.count()):

            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( rgb[0],rgb[1],rgb[2] ))

        time.sleep(wait)
        pixels.show()

def brightness_decrease(pixels, wait=0.002, step=1):
    for j in range(int(256 // step)):
        for i in range(pixels.count()):
            r, g, b = pixels.get_pixel_rgb(i)
            r = int(max(0, r - step))
            g = int(max(0, g - step))
            b = int(max(0, b - step))
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( r, g, b ))
        pixels.show()
        if wait > 0:
            time.sleep(wait)

def color_effect(pixels, color):

	#could be cooler, will do for the moment

    for i in range(3):

        brightness_decrease(pixels)
        increase_to_color(pixels, color = color)

parser = argparse.ArgumentParser(description='takes r g b values as args')

parser.add_argument('r', )
parser.add_argument('g', )
parser.add_argument('b', )

args = parser.parse_args()

color = [int(parser.r),int(parser.g),int(parser.b)]

color_effect(pixels, color)