Raspberry-Pi Prerequisites
==========================
*Please run the following commands to setup the raspberry pi for code deployment*


.. note::

    Connect to a display using HDMI to run the code

    Raspberry Pi password = ``raspberry``

Power Supply
*******************

Use the included battery bank for power supply


Update distribution packages
****************************

*First lets update your distribution packages*

``sudo apt-get update;``

``sudo apt-get upgrade;``

``sudo reboot;``

Install git, python3 & pip
**************************

*Next run the following commands to install git, python3 & pip*

.. attention::

   *Python3 is required*

``sudo apt-get install -y python3 git python3-pip``

Install CRICKIT Python3 lib.
****************************

*Next run the following commands to install CRICKIT Python 3 libraries*

``sudo pip3 install RPI.GPIO adafruit-blinka``


Install smbus i2c-tools
***********************

*Next run the following commands to add SMBus and I2C support to Python*

``sudo apt-get install python-smbus;``

``sudo apt-get install -y i2c-tools``

I2C Kernal Support
******************

*Installing Kernel Support for I2C devices*

*Run the following command for gui interface*

``sudo raspi-config``

On the GUI select **Interfacing Options** followed by **I2C**

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/045/258/medium800/learn_raspberry_pi_interfacing.png?1502764684

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/022/832/medium800/learn_raspberry_pi_i2c.png?1423001363

*When prompted to Enable I2C select ``yes``*

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/022/834/medium800/learn_raspberry_pi_wouldyoukindly.png?1423001393

*Reboot device to ensure I2C device support*

*To reboot run the following command*

``sudo reboot``

*Upon boot run the following command to see all the connected devices*

``sudo i2cdetect -y 1``

*it should show up at 0x40 (binary 1000000) as follows:*

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/022/057/medium800/raspberry_pi_i2cdetect.png?1420234437


Install adafruit-circuitpython-crickit
**************************************

*To interact with the servos, install adafruit-circuitpython-crickit by running the following command*

``sudo pip3 install adafruit-circuitpython-crickit``


Run all at once
***************

.. code-block:: bash

   # Installations
   sudo apt-get update;
   sudo apt-get upgrade;
   sudo reboot;
   sudo apt-get install -y python3 git python3-pip;
   sudo pip3 install RPI.GPIO adafruit-blinka;
   sudo apt-get install python-smbus;
   sudo apt-get install -y i2c-tools;
   # User input is required [select Interfacing Options>>I2C>>yes]
   sudo raspi-config;

   # Need to run separately
   sudo reboot;
   sudo i2cdetect -y 1


.. __: https://learn.adafruit.com/adafruit-crickit-hat-for-raspberry-pi-linux-computers/overview

.. hint::
   *For more help, refer to* `adafruit's`__ *website for further guidance*

