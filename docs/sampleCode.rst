Sample code
============
*Sample code utilizing minilib package*


*Test driving*

.. code-block:: python
    :emphasize-lines: 1

    from miniLib import Joystick, Drive, Motor

    left = Motor.Motor(0)
    right = Motor.Motor(1)
    jstick = Joystick.Joystick(0)
    robot = Drive.ArcadeDrive(left, right)

    while True:
        forwardAxis = jstick.getAxis(1)
        steerAxis = jstick.getAxis(3)
        robot.drive(forwardAxis, steerAxis)

*Test Motors*
    import time
    from miniLib import Motor

    # make two variables for the motors to make code shorter to type
    motor_1 = Motor(0)
    motor_2 = Motor(1)

    while True:
        motor_1.throttle = 1  # full speed forward
        motor_2.throttle = -1 # full speed backward
        time.sleep(1)

        motor_1.throttle = 0.5  # half speed forward
        motor_2.throttle = -0.5 # half speed backward
        time.sleep(1)

        motor_1.throttle = 0  # stopped
        motor_2.throttle = 0  # also stopped
        time.sleep(1)

        motor_1.throttle = -0.5  # half speed backward
        motor_2.throttle = 0.5   # half speed forward
        time.sleep(1)

        motor_1.throttle = -1  # full speed backward
        motor_2.throttle = 1   # full speed forward
        time.sleep(1)

        motor_1.throttle = 0  # stopped
        motor_2.throttle = 0  # also stopped
        time.sleep(0.5)