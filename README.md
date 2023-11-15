# Tagespaul 2.0

This is my fun raspberry pi project, which is based on the tagespaul app https://www.let-verlag.de/tagesspruch
Originally this was developed as a birthday present to my girlfriend.

# Gist

## Hardware


The tagespaul 2.0 is powered by a raspberry pi 3.0 which is connected to 4 buttons and a chain of LED lights as well as a small 
sound system. The pi is embedded in a round plastic box (old protein chake) and sourrounded by a lantern. 
This raspberry pi supports wifi, which allows to update the software as well as the sound via SSH.
 
## Software

The tagespaul loop continously runs a color program for the LED lights and listens to button triggers. Ones a button is triggered it activates one of 
4 different sound options and color programs. The sound is randomly taken from a choice stored in `sounds\*` and is different every day. 
The PI checks the date via Wifi.

### Color program

### Sound program

# TODO 

* fix sound folder