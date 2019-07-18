Prerequisites
==============
*Please run the following commands to setup the raspberry pi for code deployment*

Update distribution packages
****************************

*First lets update your distribution packages*

``sudo apt update; sudo apt upgrade``

Install smbus i2c-tools
***********************

*Next run the following commands to add SMBus and I2C support to Python*

``sudo apt-get install python-smbus``
``sudo apt-get install i2c-tools``

I2C Kernal Support
******************

*Installing Kernel Support for I2C devides*

*Run the following command for gui interface*

``sudo raspi-config``

*On the GUI select ``Interfacing Options`` followed by ``I2C``*

*When promped to Enable I2C select ``yes``*

*Reboot device to ensure I2C device support*

*To reboot run the following command*

``sudo reboot``

*Upon boot run the following command to see all the connected devices*

``sudo i2cdetect -y 1``

Install adafruit-servokit
*************************

*To interact with the servos install adafruit-servokit by running the following command*

``sudo pip3 install adafruit-circuitpython-servokit``