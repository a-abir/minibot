class ArcadeDrive:
    def __init__(self, left, right):
        '''
        Setup Arcade drive

        :param left: left side drive
        :type right: continuous_servo
        :param rightServo: right side drive
        :type rightServo: continuous_servo
        '''
        self.left = left
        self.right = right

    def calculate(self, forward, steer):
        '''
        Internal function to calculate the left and right power

        :param forward: forward power
        :type forward: float
        :param steer: steer power
        :type steer: float
        :return: tuple of floats: power for left and right drive
        :rtype: tuple
        '''

        # calculate left and right power
        leftPower = forward - steer
        rightPower = forward + steer
        return leftPower, rightPower

    def drive(self, forwardPower, steerPower):
        '''
        Drive given the forward and steer axis power
        Meant to be run inside a while loop

        :param forwardPower: Forward power from joystick axis
        :type forwardPower: float
        :param steerPower: Steer power from joystick axis
        :type steerPower: float
        '''
        self.leftPower, self.rightPower = self.calculate(forwardPower, steerPower)
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
        self.left.throttle(self.leftPower)
        self.right.throttle(self.rightPower)