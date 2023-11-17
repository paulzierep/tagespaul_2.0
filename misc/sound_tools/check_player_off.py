import subprocess
import os
import time
from datetime import datetime
import random

def play_sound_by_button(sound_type = None):

    if sound_type == 'nasty':
        s_path = os.path.join('sounds','nasty') 

    if sound_type == 'chillout':
        s_path = os.path.join('sounds','chillout') 

    if sound_type == 'random':
        s_path = os.path.join('sounds','random') 

    if sound_type == 'tagespaul':
        s_path = os.path.join('sounds','tagespaul') 

    day_of_year = datetime.now().timetuple().tm_yday

    files = list(os.listdir(s_path))

    random.seed(42) #I do not know, but this needs to be set here or the sound will not be random 
    random.shuffle(files)

    file_id = day_of_year % len(files)  #modulo repeats the file_id each time the end of the end of the list is reached 

    file = files[file_id]

    sound_path = os.path.join(s_path, file)

    return(play_sound_in_bg(sound_path))

def play_sound_in_bg(SOUND_PATH):

    with open('player_out.txt', "w") as outfile:

        player = subprocess.Popen(
            ["mplayer", "-volume", "100", SOUND_PATH], 
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

player = play_sound_by_button(sound_type = 'chillout')

while True:

    # print(output)

    print(check_player(player))

    print('call')

    time.sleep(5)