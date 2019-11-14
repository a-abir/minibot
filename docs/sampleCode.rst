Sample code
============
*Sample code utilizing minilib package*


``Test driving``

.. code-block:: python
    :emphasize-lines: 1

    from minilib import Joystick, ArcadeDrive, Motor

    left = Motor(0)
    right = Motor(1)
    jstick = Joystick(0)
    robot = ArcadeDrive(left, right)

    while True:
        forwardAxis = jstick.getAxis(1)
        steerAxis = jstick.getAxis(3)
        robot.drive(forwardAxis, steerAxis)

-----------

``Test Motors``

.. code-block:: python
    :emphasize-lines: 2

    import time
    from minilib import Motor

    motor_1 = Motor(0)
    motor_2 = Motor(1)

    for _ in range(3):
        motor_1.throttle(1)
        motor_2.throttle(-1)
        time.sleep(1)

        motor_1.throttle(-0.5)
        motor_2.throttle(0.5)
        time.sleep(1.5)

        motor_1.throttle(1)
        motor_2.throttle(-1)
        time.sleep(1)

-----------

``Test Servos``

.. code-block:: python
    :emphasize-lines: 2

    import time
    from minilib import Servo

    servo_1 = Servo(0)
    servo_2 = Servo(1)

    for _ in range(3):
        servo_1.angle(180)
        servo_2.angle(-180)
        time.sleep(1)

        servo_1.angle(-90)
        servo_2.angle(90)
        time.sleep(1.5)

        servo_1.angle(180)
        servo_2.angle(-180)
        time.sleep(1)

