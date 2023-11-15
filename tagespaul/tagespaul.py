#basic modules
import time
import random
import subprocess
import os
import signal
from datetime import datetime

# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO 

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

random.seed(42)

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

def rainbow_colors_offset(pixels, wait=0.05, offset = 3): #17 is full wheel, 3 is slow
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

def set_rainbow_colors_offset(pixels, j, wait=0.05, offset = 17):
    for i in range(pixels.count()):
        pixels.set_pixel(i, wheel(((256 // pixels.count() + j + (i * offset) )) % 256) )
    pixels.show()
    if wait > 0:
        time.sleep(wait)



# def appear_from_back(pixels, color=(255, 0, 0)):
#     for i in range(pixels.count()):
#         for j in reversed(range(i, pixels.count())):
#             pixels.clear()
#             # first set all pixels at the begin
#             for k in range(i):
#                 pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
#             # set then the pixel at position j
#             pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color( color[0], color[1], color[2] ))
#             pixels.show()
#             time.sleep(0.02)


# def rotate_colors(pixels, color=(255, 0, 0)):

#     for k in range(100):

#         for i in range(pixels.count()):
#             pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0,0,0))

#         k1 = (k % 15)
#         #print(k1)
#         pixels.set_pixel(k1, Adafruit_WS2801.RGB_to_color(color[0],color[1],color[2]))
#         k2 = ((k + 1) % 15)
#         #print(k2)
#         pixels.set_pixel(k1, Adafruit_WS2801.RGB_to_color(color[0],color[1],color[2]))
#         k3 = ((k + 2) % 15)
#         #print(k3)
#         pixels.set_pixel(k2, Adafruit_WS2801.RGB_to_color(color[0],color[1],color[2]))
#         pixels.show()
#         time.sleep(0.1)

def increase_to_color(pixels, j, color = [0,0,256]):

    print(color)

    j = j % (256 * 2)

    # for j in range(256):

    #color goes up
    if j <= 256:

        rgb = [
        int(color[0] / 256 * j), 
        int(color[1] / 256 * j), 
        int(color[2] / 256 * j)
        ]

        # print(rgb)

        for i in range(pixels.count()):

            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( rgb[0],rgb[1],rgb[2] ))

        # time.sleep(wait)
        pixels.show()

    #color goes down
    step = 1
    if j >= 256:

        for i in range(pixels.count()):

            r, g, b = pixels.get_pixel_rgb(i)

            rgb = [
            int(max(0, r - step)),
            int(max(0, g - step)),
            int(max(0, b - step)),
            ]

            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( rgb[0],rgb[1],rgb[2] ))

        pixels.show()

    print(rgb)

def add_range(x, add = 30, wheel = 256):

    # random.seed(42)

    # if bool(random.getrandbits(1)):

    #     x = x + random.randint(0,add)

    # else:

    #     x = x - random.randint(0,add)

    x = x + add

    x = x % wheel

    return(x)

def flimmer(color):

    color2 = [0,0,0]

    for i in range(3):

        color2[i] = add_range(color[i])

    return(color2)


def random_dots(pixels, j, color = [0,0,256]):

    if j % 2 == 0: #do this onle every 10th iteration

        color_f = flimmer(color)

        print(color)
        print(color_f)

        for i in range(pixels.count()):

            if bool(random.getrandbits(1)):

                # color_f = flimmer(color)

                # print(color_f)

                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( color[0],color[1],color[2]))

            else:

                pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color( color_f[0],color_f[1],color_f[2] ))

        pixels.show()


def color_effect(pixels, j, color):

    increase_to_color(pixels, j, color)

    # random_dots(pixels, j, color)

    #could be cooler, will do for the moment

    # for i in range(3):

    #     brightness_decrease(pixels)
    #     increase_to_color(pixels, color = color)

###########################
#Sound Utility funcs
###########################

script_path = os.path.dirname(os.path.realpath(__file__))

def play_sound_by_button(sound_type = None):

    if sound_type == 'nasty':
        s_path = os.path.join(script_path,'sounds','nasty') 

    if sound_type == 'chillout':
        s_path = os.path.join(script_path,'sounds','chillout') 

    if sound_type == 'random':
        s_path = os.path.join(script_path,'sounds','random') 

    if sound_type == 'tagespaul':
        s_path = os.path.join(script_path,'sounds','tagespaul') 

    day_of_year = datetime.now().timetuple().tm_yday

    files = list(os.listdir(s_path))

    random.seed(42) #I do not know, but this needs to be set here or the sound will not be random 
    random.shuffle(files)

    file_id = day_of_year % len(files)  #modulo repeats the file_id each time the end of the end of the list is reached 

    file = files[file_id]

    sound_path = os.path.join(s_path, file)

    return(play_sound_in_bg(sound_path))

def play_sound_in_bg(SOUND_PATH):

    with open(os.path.join(script_path, 'player_out.txt'), "w") as outfile:

        player = subprocess.Popen(
            ["mplayer", "-volume", "85", SOUND_PATH], 
            # stdin=subprocess.PIPE, 
            stdout=outfile, 
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid, #add id
            )

    return(player)

def stop_sound(player):
    if player:
        os.killpg(os.getpgid(player.pid), signal.SIGTERM)  # Send the signal to all the process groups

def check_player(player):

    if not player:
        return(False, False)

    poll = player.poll()
    if poll == None:
        return(True, player)
    else:
        return(False, False)

###########################
#GBIO utils
###########################

def button_call(gpio_mapping, GPIO, color, player, j):

    # color = None
    # player = None

    for gpio_id in gpio_mapping.keys():

        if GPIO.input(gpio_id) == GPIO.HIGH:

            #stop last player
            stop_sound(player)

            #play sound func
            player = play_sound_by_button(sound_type = gpio_mapping[gpio_id]['sound'])

            color = gpio_mapping[gpio_id]['color']
            j = 0

            print("Button {0} was pushed!".format(gpio_id))
            time.sleep(0.2)

    return(color, player, j)


###########################
#Run tagespaul
###########################

wait=0.05
player = None
play_color_effect = None
color = [0,0,256]

gpio_mapping = {
    26:
    {
    'sound':'nasty',
    'color':[19,54,229],
    },
    19:
    {
    'sound':'random',
    'color':[230,18,18],
    },
    13:
    {
    'sound':'tagespaul',
    'color':[128,255,0],
    },
    6:
    {
    'sound':'chillout',
    'color':[246,246, 63],
    },
}

j = 0
while True: # Run forever

    ###########################
    #Show the color stuff, the functions must change with j
    ###########################

    time.sleep(wait)    

    if play_color_effect:
        # print(color)
        # exit()

        color_effect(pixels, j, color)
    else:
        set_rainbow_colors_offset(pixels,j)

    j += 1

    color, player, j = button_call(gpio_mapping, GPIO, color, player, j)

    play_color_effect, player = check_player(player)

    # if GPIO.input(26) == GPIO.HIGH:

    #     #stop last player
    #     stop_sound(player)

    #     #play sound func
    #     player = play_sound_by_button(sound_type = 'nasty')

    #     #play color func
    #     # rotate_colors(pixels, color = (0,204,0))

    #     play_color_effect = True
    #     color = [0,0,256]

    #     # color_effect(pixels, color = [0,0,256])

    #     print("Button 26 was pushed!")
    #     time.sleep(0.2)

    # if GPIO.input(19) == GPIO.HIGH:

    #     #stop last player
    #     stop_sound(player)

    #     #play sound func
    #     player = play_sound_by_button(sound_type = 'random')
        
    #     play_color_effect = True
    #     color = [0,0,256]

    #     #play color func
    #     color_effect(pixels, color = [256,0,0])

    #     print("Button 19 was pushed!")
    #     time.sleep(0.2)

    # if GPIO.input(13) == GPIO.HIGH:

    #     #stop last player
    #     stop_sound(player)

    #     #play sound func
    #     player = play_sound_by_button(sound_type = 'tagespaul')

    #     #play color func
    #     color_effect(pixels, color = [128,255,0])

    #     print("Button 13 was pushed!")
    #     time.sleep(0.2)

    # if GPIO.input(6) == GPIO.HIGH:

    #     #stop last player
    #     stop_sound(player)

    #     #play sound func
    #     player = play_sound_by_button(sound_type = 'chillout')

    #     #play color func
    #     color_effect(pixels, color = [255,255, 153])

    #     # set_color_blink(pixels,192)
    #     print("Button 6 was pushed!")
    #     time.sleep(0.2)
