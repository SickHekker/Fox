# Fox

It's very simple code but it works so there is no reason to overcomplicate it.
in order to get the files for the motorcontroller you need to do the following commands, i got these from the adafruit tutorial.

sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus git
cd ~
git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
git clone https://github.com/SickHekker/Fox.git
cd Adafruit-Motor-HAT-Python-Library
sudo python setup.py install
cd ~
cd Fox
sudo python fox.py
