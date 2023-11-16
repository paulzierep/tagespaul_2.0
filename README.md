# Tagespaul 2.0

This is my fun raspberry pi project, which is based on the Tagespaul app https://www.let-verlag.de/tagesspruch
Originally, this was developed as a birthday present to my girlfriend.

# Gist

## Hardware


The Tagespaul 2.0 is powered by a raspberry pi 3.0 which is connected to 4 buttons and a chain of LED lights as well as a small 
sound system. The pi is embedded in a round plastic box (old protein shake) and surrounded by a lantern. 
This raspberry pi supports wifi, which allows to update the software as well as the sound via SSH.
 
## Software

The Tagespaul loop continuously runs a color program for the LED lights and listens to button triggers. Ones a button is triggered it activates one of 
4 different sound options and color programs. The sound is randomly taken from a choice stored in `sounds\*` and is different every day. 
The PI checks the date via Wifi.

### Color program

### Sound program

# Set-up
## Prepare the PI

Connect a screen, mouse and keyboard to the PI and setup the [wifi](https://www.seeedstudio.com/blog/2021/01/25/three-methods-to-configure-raspberry-pi-wifi/) and enable ssh.
Get the IP address of the PI with:

```
ifconfig wlan0
```

## Copy data to the PI 
### Install the copy2rpi script on a computer in the same wifi

* Install the requirements to run the copy2rpi.py script with conda/mamba

    ```bash
    mamba create --name tagespaul-remote --file requirements.txt
    ```

* Add the PI IP address in the `.env` file.

### Run the copy2rpi script with

```bash
mamba activate tagespaul-remote
python copy2rpi.py
```
Each time you update this folder, e.g. when you add/change the sounds, you can
update the folder on the PI with this script.

## SSH on the PI and setup the script

### Install requirements on PI

```bash
cd /home/pi/Projects/tagespaul_2.0/
pip install -r requirements_PI.txt
```

### Run scrip on start-up

To run the script on PI startup add this text to the `/etc/rc.local` file with:

```bash
sudo nano /etc/rc.local
```

```txt
sudo -H -u pi /usr/bin/python3 /home/pi/Projects/tagespaul_2.0/tagespaul/tagespaul.py > /home/pi/Projects/tagespaul_2.0/tagespaul/log.txt 2>&1

exit 0
```

And make `/etc/rc.local` executable with:

```
sudo chmod +x /etc/rc.local
```


# TODO 

* fix sound folder
* PI pi set