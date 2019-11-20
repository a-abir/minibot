class ArcadeDrive:
    def __init__(self, left, right, a=0, b=1):
        '''
        Setup Arcade drive

        :param left: left side drive
        :type right: continuous_servo
        :param rightServo: right side drive
        :type rightServo: continuous_servo
        '''
        self.left = left
        self.right = right
	self.a = a
	self.b = b

    def calculate(self, fwd, rcw, a, b):
        '''
        Arcade algorithm to compute left and right wheel commands
        from forward and rotate-clockwise joystick commands.

        a=0 and b=1 provides the WPILib arcade behavior.

        :param fwd: Forward command (-1 to +1)
        :type fwd: float
        :param turn: Rotate command (-1 to +1)
        :type turn: float
        :param a: amount to turn at 100% fwd in the range 0 to 1, defaults to 0
        :type a: int, optional
        :param b: amount to turn at   0% fwd in the range 0 to 1, defaults to 1
        :type b: int, optional
        :return: leftPower, rightPower
        :rtype: (float, float)
        '''
        def L(fwd, turn, a, b): return fwd + b*turn*(1-fwd)
        def R(fwd, rcw, a, b): return fwd - b*rcw + fwd*rcw*(b-a-1)
        if fwd >= 0:
            if rcw >= 0:
                left = L(fwd, rcw, a, b)
                right = R(fwd, rcw, a, b)
            else:
                left = R(fwd, -rcw, a, b)
                right = L(fwd, -rcw, a, b)
        else:
            if rcw >= 0:
                left = -R(-fwd, rcw, a, b)
                right = -L(-fwd, rcw, a, b)
            else:
                left = -L(-fwd, -rcw, a, b)
                right = -R(-fwd, -rcw, a, b)
        return left, right

    def drive(self, forwardPower, steerPower):
        '''
        Drive given the forward and steer axis power
        Meant to be run inside a while loop

        :param forwardPower: Forward power from joystick axis
        :type forwardPower: float
        :param steerPower: Steer power from joystick axis
        :type steerPower: float
        '''
        self.leftPower, self.rightPower = self.calculate(
            forwardPower, steerPower, self.a, self.b)
        self.left.throttle(self.leftPower)
        self.right.throttle(self.rightPower)


class TankDrive:
    def __init__(self, left, right):
        '''
        Setup Tank drive

        :param LeftServo: Servo for the left side drive
        :type LeftServo: continuous_servo
        :param rightServo: Servo for the right side drive
        :type rightServo: continuous_servo
        '''
        self.left = left
        self.right = right

    def drive(self, leftPower, rightPower):
        '''
        Drive given the left and right axis power
        Meant to be run inside a while loop

        :param leftPower: Forward power from joystick axis
        :type leftPower: float
        :param rightPower: Steer power from joystick axis
        :type rightPower: float
        '''
        self.left.throttle(leftPower)
        self.right.throttle(rightPower)
