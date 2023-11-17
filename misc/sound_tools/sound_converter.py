import os
import subprocess

def convert_sound(SOUND_PATH):

    OUT_PATH = SOUND_PATH.replace('.ogg', '.mp3')

    player = subprocess.Popen(
        ["ffmpeg", "-i", SOUND_PATH, OUT_PATH], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid, #add id
        )

SOUND_FOLDER = 'convert_sound'

for file in os.listdir(SOUND_FOLDER):
    s_path = os.path.join(SOUND_FOLDER, file)
    convert_sound(s_path)