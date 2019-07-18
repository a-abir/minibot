# minibot

### `Setup Raspberry pi for depolyment`
sudo apt update
sudo apt upgrade

sudo apt-get install python-smbus
sudo apt-get install i2c-tools

sudo raspi-config #Interfacing Options>>I2C>>Enable

sudo pip3 install adafruit-circuitpython-servokit

sudo reboot

sudo i2cdetect -y 1

### `Make the raspberry pi to image Win32DiskImager`