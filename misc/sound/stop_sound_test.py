#basic modules
import time
import random
import subprocess
import os
import signal

import sys
print(sys.version)

###########################
#Sound Utility funcs
###########################

def play_sound_in_bg(SOUND_PATH):
    player = subprocess.Popen(
        ["mplayer", "-volume", "100", SOUND_PATH], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid,
        # encoding='utf8'
        )
    return(player)

mc = os.path.join('mc.m4a')

def stop_sound(player):
    os.killpg(os.getpgid(player.pid), signal.SIGTERM)  # Send the signal to all the process groups


player = play_sound_in_bg(mc)

# while player.poll() is None:
#     l = player.stdout.readline() # This blocks until it receives a newline.
#     r = player.stderr.readline() # This blocks until it receives a newline.
#     print(l)

time.sleep(2)

print('bbbbm')

time.sleep(2)

stop_sound(player)