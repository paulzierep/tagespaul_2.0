import os
import shutil
import subprocess

from dotenv import load_dotenv

# load the envs from .env
load_dotenv()

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
PI_IP = os.getenv("PI_IP")

PC_DATA_FOLDER = (
    os.path.join(SCRIPT_PATH) + "/"
)  # the / implies to copy the src folder into the dst folder, not as as subfolder
PI_DATA_FOLDER = f"pi@{PI_IP}:~/Projects/tagespaul_2.0/"

################################
# Copy data to py
################################

print("*********** copy data to PI ***********")

sub_string = "rsync -av -e ssh {0} {1}".format(
    PC_DATA_FOLDER,
    PI_DATA_FOLDER,
)

print(sub_string)

sub_report = subprocess.call(sub_string, shell=True)
print(sub_report)

# print('*********** copy data from PI ***********')

# sub_string = 'rsync -av -e ssh {0} {1}'.format(
# 	PI_DATA_FOLDER,
# 	PC_DATA_FOLDER,
# 	)

# print(sub_string)
# sub_report = subprocess.call(sub_string, shell = True)
# print(sub_report)
