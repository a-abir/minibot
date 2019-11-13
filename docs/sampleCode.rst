Sample code
============
*Sample code utilizing minilib package*

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
