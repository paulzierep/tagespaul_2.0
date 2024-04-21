# basic modules
import os
import random
import signal
import subprocess
import time
from datetime import datetime

import Adafruit_GPIO.SPI as SPI

# Import the WS2801 module.
import Adafruit_WS2801

# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO

random.seed(42)

###########################
# LEDs
###########################

# Configure the count of pixels:
PIXEL_COUNT = 15

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

###########################
# Buttons
###########################

# GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(
    26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN
)  # Set pin 26 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(
    19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN
)  # Set pin 26 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(
    13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN
)  # Set pin 26 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(
    6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN
)  # Set pin 26 to be an input pin and set initial value to be pulled low (off)

###########################
# Color Utility funcs
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


def set_rainbow_colors_offset(pixels, j, wait=0.001, offset=17):
    """
    Make a rainbow that rotates around the lights

    :pixels: the pixels object
    :j: the time point
    :wait:the speed of the rainbow
    :offset: the rainbow offset (distance of colors between lights)
    """
    for i in range(pixels.count()):
        pixels.set_pixel(i, wheel(((256 // pixels.count() + j + (i * offset))) % 256))
    pixels.show()
    if wait > 0:
        time.sleep(wait)


def increase_to_color(pixels, j, color=[0, 0, 256]):
    """
    Make the light fade in and out on a specific color

    :pixels: the pixels object
    :j: the time point
    :color:the color to use
    """

    j = j % (256 * 2)

    # for j in range(256):

    # color goes up
    if j <= 256:
        rgb = [
            int(color[0] / 256 * j),
            int(color[1] / 256 * j),
            int(color[2] / 256 * j),
        ]

        # print(rgb)

        for i in range(pixels.count()):
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(rgb[0], rgb[1], rgb[2]))

        # time.sleep(wait)
        pixels.show()

    # color goes down
    step = 1
    if j >= 256:
        for i in range(pixels.count()):
            r, g, b = pixels.get_pixel_rgb(i)

            rgb = [
                int(max(0, r - step)),
                int(max(0, g - step)),
                int(max(0, b - step)),
            ]

            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(rgb[0], rgb[1], rgb[2]))

        pixels.show()

    print("Color: ", rgb)


def color_effect(pixels, j, color):
    """
    Middleman function that runs the color function

    :pixels: the pixels object
    :j: the time point
    :color:the color to use
    """
    increase_to_color(pixels, j, color)


###########################
# Sound Utility funcs
###########################

script_path = os.path.dirname(os.path.realpath(__file__))
sounds_folder = os.path.join(script_path, "sounds")

###########################
# Download news podcast on startup
###########################


def download_news():
    tpaul_path = os.path.join(sounds_folder, "tagespaul")
    with open(os.path.join(script_path, "youtube_dl_out.txt"), "w") as outfile:
        player = subprocess.Popen(
            [
                "youtube-dl",
                "https://www.deutschlandfunk.de/nachrichten-108.xml",
                "--playlist-items",
                "1",
                "-o",
                f"{tpaul_path}/news.mp3",
            ],
            # stdin=subprocess.PIPE,
            stdout=outfile,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid,  # add id
        )


download_news()


def play_sound_by_button(sound_type=None):
    s_path = os.path.join(sounds_folder, sound_type)

    day_of_year = datetime.now().timetuple().tm_yday

    files = list(os.listdir(s_path))

    random.seed(42)  # Needs to be set here or the sound will not be random
    random.shuffle(files)

    file_id = day_of_year % len(files)  # modulo repeats the file_id each time the end of the list is reached

    file = files[file_id]

    sound_path = os.path.join(s_path, file)

    return play_sound_in_bg(sound_path)


def play_sound_in_bg(SOUND_PATH):
    with open(os.path.join(script_path, "player_out.txt"), "w") as outfile:
        player = subprocess.Popen(
            ["mplayer", "-volume", "85", SOUND_PATH],
            # stdin=subprocess.PIPE,
            stdout=outfile,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid,  # add id
        )

    return player


def stop_sound(player):
    if player:
        os.killpg(os.getpgid(player.pid), signal.SIGTERM)  # Send the signal to all the process groups


def check_player(player):
    if not player:
        return (False, False)

    poll = player.poll()
    if poll == None:
        return (True, player)
    else:
        return (False, False)


###########################
# GBIO utils
###########################


def button_call(gpio_mapping, GPIO, color, player, j):
    # color = None
    # player = None

    for gpio_id in gpio_mapping.keys():
        if GPIO.input(gpio_id) == GPIO.HIGH:
            # stop last player
            stop_sound(player)

            # play sound func
            player = play_sound_by_button(sound_type=gpio_mapping[gpio_id]["sound"])

            color = gpio_mapping[gpio_id]["color"]
            j = 0

            print("Button {0} was pushed!".format(gpio_id))
            time.sleep(0.2)

    return (color, player, j)


###########################
# Run tagespaul
###########################

wait = 0.05
player = None
j = 0
do_color_effect = True
color = [0, 0, 256]

gpio_mapping = {
    26: {
        "sound": "nasty",
        "color": [19, 54, 229],
    },
    19: {
        "sound": "random",
        "color": [230, 18, 18],
    },
    13: {
        "sound": "tagespaul",
        "color": [128, 255, 0],
    },
    6: {
        "sound": "chillout",
        "color": [246, 246, 63],
    },
}


while True:  # Run forever
    ###########################
    # Show the color stuff, the functions must change with j
    ###########################

    time.sleep(wait)

    if do_color_effect:
        color_effect(pixels, j, color)
    else:
        set_rainbow_colors_offset(pixels, j)

    j += 1

    color, player, j = button_call(gpio_mapping, GPIO, color, player, j)

    do_color_effect, player = check_player(player)
