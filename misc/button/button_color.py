import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import random


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

###########################
#Color Utility funcs
###########################

# Define the wheel function to interpolate between different hues.
def wheel(pos):
    if pos < 85:
        return Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Adafruit_WS2801.RGB_to_color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Adafruit_WS2801.RGB_to_color(0, pos * 3, 255 - pos * 3)

def rainbow_colors(pixels, wait=0.05):
    for j in range(256): # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)

def rainbow_colors_range(pixels, wait=0.05, start = 0, end = 64):

    for j in range(start, end): # one cycle of all 256 colors in the wheel
        print(j)
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)

    for j in reversed(range(start, end)): # one cycle of all 256 colors in the wheel
        print(j)
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)


def rainbow_colors_offset(pixels, wait=0.05, offset = 1): #17 is full wheel, 3 is slow
    for j in range(256): # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j + (i * offset) )) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)

def rainbow_colors_random(pixels, wait=0.05):
    for j in range(100):
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + (random.randint(0,10)))) % 256) )
        pixels.show()
        if wait > 0:
            time.sleep(wait)

def set_color_blink(pixels, color = 1):
    print(color)
    for k in range(20):
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + color)) % 256) )
        pixels.show()
        time.sleep(0.1)
        for i in range(pixels.count()):
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( 0,0,0 ))
        pixels.show()
        time.sleep(0.1)
        print(k)

def set_color(pixels, color = 1):
    print(color)
    for i in range(pixels.count()):
        pixels.set_pixel(i, wheel(((256 // pixels.count() + color)) % 256) )
    pixels.show()

def brightness_decrease(pixels, wait=0.01, step=1):
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

def set_rainbow_colors_offset(pixels, j, wait=0.05, offset = 10):
    for i in range(pixels.count()):
        pixels.set_pixel(i, wheel(((256 // pixels.count() + j + (i * offset) )) % 256) )
    pixels.show()
    if wait > 0:
        time.sleep(wait)

def appear_from_back(pixels, color=(255, 0, 0)):
    for i in range(pixels.count()):
        for j in reversed(range(i, pixels.count())):
            pixels.clear()
            # first set all pixels at the begin
            for k in range(i):
                pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
            # set then the pixel at position j
            pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
            pixels.show()
            time.sleep(0.02)


def rotate_colors(pixels, color=(255, 0, 0)):

    for k in range(100):

        for i in range(pixels.count()):
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0,0,0))

        k1 = (k % 15)
        print(k1)
        pixels.set_pixel(k1, Adafruit_WS2801.RGB_to_color(color[0],color[1],color[2]))
        k2 = ((k + 1) % 15)
        print(k2)
        pixels.set_pixel(k1, Adafruit_WS2801.RGB_to_color(color[0],color[1],color[2]))
        k3 = ((k + 2) % 15)
        print(k3)
        pixels.set_pixel(k2, Adafruit_WS2801.RGB_to_color(color[0],color[1],color[2]))
        pixels.show()
        time.sleep(0.1)



    # for i in range(pixels.count()):
    #     for j in reversed(range(i, pixels.count())):
    #         pixels.clear()
    #         # first set all pixels at the begin
    #         for k in range(i):
    #             pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
    #         # set then the pixel at position j
    #         pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
    #         pixels.show()
    #         time.sleep(0.02)




j = 0
while True: # Run forever

    set_rainbow_colors_offset(pixels,j)
    j += 1

    if GPIO.input(26) == GPIO.HIGH:
        # set_color_blink(pixels,0)
        rotate_colors(pixels, color = (0,204,0))
        print("Button 26 was pushed!")
        time.sleep(0.2)

    if GPIO.input(19) == GPIO.HIGH:

        #set_color_blink(pixels,30)
        
        rotate_colors(pixels, color = (255,255,204))
        print("Button 19 was pushed!")
        time.sleep(0.2)

    if GPIO.input(13) == GPIO.HIGH:

        # set_color_blink(pixels,128)
        rotate_colors(pixels, color = (255,0,0))
        print("Button 13 was pushed!")
        time.sleep(0.2)

    if GPIO.input(6) == GPIO.HIGH:

        rotate_colors(pixels, color = (51, 51, 204))
        # set_color_blink(pixels,192)
        print("Button 6 was pushed!")
        time.sleep(0.2)
