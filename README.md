# Fox

It's very simple code but it works so there is no reason to over complicate it.
In order to get the files for the motorcontroller you need to do the following commands.
I got these from the Adafruit tutorial and added the commands to use my code

Don't forget to enable i2c in raspi-config

```bash
sudo apt-get update

sudo apt-get install build-essential python-dev python-smbus git

cd

git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git

git clone https://github.com/SickHekker/Fox.git

cd Adafruit-Motor-HAT-Python-Library

sudo python setup.py install

cd ~

cd Fox

sudo python fox.py
```

You can use W A S D to drive the tank.
And E to stop it.
the keys 1 until 5 are diffrent speeds.
the keys R T Y are to change the speed at which the tank turns.

To stream video you can use motion using a webcam.
I'm not going into detail here but make sure you disable motion detection, motion tracking and disable the function that it takes photos when motion is detected otherwise your storage will fill up with pictures

Have fun :D
