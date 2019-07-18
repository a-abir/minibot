Software Prerequisites
======================
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

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/045/258/medium800/learn_raspberry_pi_interfacing.png?1502764684

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/022/832/medium800/learn_raspberry_pi_i2c.png?1423001363

*When promped to Enable I2C select ``yes``*

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/022/834/medium800/learn_raspberry_pi_wouldyoukindly.png?1423001393

*Reboot device to ensure I2C device support*

*To reboot run the following command*

``sudo reboot``

*Upon boot run the following command to see all the connected devices*

``sudo i2cdetect -y 1``

*it should show up at 0x40 (binary 1000000) as follows:*

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/022/057/medium800/raspberry_pi_i2cdetect.png?1420234437


Install adafruit-servokit
*************************

*To interact with the servos install adafruit-servokit by running the following command*

``sudo pip3 install adafruit-circuitpython-servokit``


Run all at once
***************

.. code-block:: bash

   # Installations
   sudo apt update; sudo apt upgrade
   sudo apt-get install python-smbus
   sudo apt-get install i2c-tools
   sudo pip3 install adafruit-circuitpython-servokit
   # configurations <Requires user input>
   sudo raspi-config
   sudo reboot
   sudo i2cdetect -y 1


.. __: https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/attach-and-test-the-hat
*Refer to* `adafruit's`__ *website for furather guidence*

