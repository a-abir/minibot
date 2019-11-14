minilib Library
================

*Documentation for the Library*

``minilib.Drive.ArcadeDrive``
-----------------------------

.. class:: minilib.Drive.ArcadeDrive (self, left, right)

   .. method:: __init__(self, left, right)

      Setup Arcade drive

      :param left: left side drive
      :type right: continuous_servo
      :param rightServo: right side drive
      :type rightServo: continuous_servo

   .. method:: drive(self, forwardPower, steerPower)

      Drive given the forward and steer axis power
      Meant to be run inside a while loop

      :param forwardPower: Forward power from joystick axis
      :type forwardPower: float
      :param steerPower: Steer power from joystick axis
      :type steerPower: float



``minilib.Drive.TankDrive``
-----------------------------

.. class:: minilib.Drive.TankDrive (self, left, right)

   .. method:: __init__(self, left, right)

      Setup Arcade drive

      :param left: left side drive
      :type right: continuous_servo
      :param rightServo: right side drive
      :type rightServo: continuous_servo

   .. method:: drive(self, leftPower, rightPower)

      Drive given the left and right axis power
        Meant to be run inside a while loop

      :param leftPower: Forward power from joystick axis
      :type leftPower: float
      :param rightPower: Steer power from joystick axis
      :type rightPower: float



``minilib.Joystick.Joystick``
-----------------------------

.. class:: minilib.Joystick.Joystick (self, ID, deadband=0)

   .. method:: __init__(self, ID, deadband=0)

      Setup Joystick control using pygame
      :param id: ID of the joystick
      :type id: int

   .. method:: getAxis(self, axisID)

      Get the value of the axis

      :param axisID: Id of the axis
      :type axisID: int
      :return: value of the axis
      :rtype: float

   .. method:: getButton(self, buttonID)

      Get the state of the button

      :param buttonID: Id of the button
      :type buttonID: int
      :return: state of the button
      :rtype: bool



``minilib.Motor.Motor``
-----------------------------

.. class:: minilib.Motor.Motor (self, ID)

   .. method:: __init__(self, ID)

      Inintialize the DC Motor

      :param ID: The ID of the Motor [0,1]
      :type ID: int

   .. method:: throttle(self, power)

      Input power for the Motor

      :param power: Value from -1 to 1
      :type power: float


``minilib.Servo.Servo``
-----------------------------

.. class:: minilib.Servo.Servo (self, ID)

   .. method:: __init__(self, ID)

      Initialize a Servo

      :param ID: ID of the Servo [0,1,2,3]
      :type ID: int

   .. method:: angle(self, degree)

      Set the angle to rotate to

      :param degree: degree of the Servo
      :type degree: int


``minilib.Servo.ContiniousServo``
----------------------------------


.. class:: minilib.Servo.ContiniousServo (self, ID)

   .. method:: __init__(self, ID)

      Initialize a Continious Servo

      :param ID: ID of the Continious Servo [0,1,2,3]
      :type ID: int

   .. method:: throttle(self, power)

      Set the throttle of the Continious Servo

      :param power: Power of the Continious Servo -1 to 1
      :type power: float
