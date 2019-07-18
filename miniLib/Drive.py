class ArcadeDrive:
    def __init__(self, LeftServo, rightServo):
        '''
        Setup Arcade drive

        :param LeftServo: Servo for the left side drive
        :type LeftServo: continuous_servo
        :param rightServo: Servo for the right side drive
        :type rightServo: continuous_servo
        '''
        self.right = rightServo
        self.left = LeftServo

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
        leftPower = forward + steer
        rightPower = forward - steer
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
        self.left.throttle = self.leftPower
        self.right.throttle = self.rightPower


class TankDrive:
    def __init__(self, LeftServo, rightServo):
        '''
        Setup Tank drive

        :param LeftServo: Servo for the left side drive
        :type LeftServo: continuous_servo
        :param rightServo: Servo for the right side drive
        :type rightServo: continuous_servo
        '''
        self.right = rightServo
        self.left = LeftServo

    def drive(self, leftPower, rightPower):
        '''
        Drive given the forward and steer axis power
        Meant to be run inside a while loop

        :param leftPower: Forward power from joystick axis
        :type leftPower: float
        :param rightPower: Steer power from joystick axis
        :type rightPower: float
        '''
        self.left.throttle = self.leftPower
        self.right.throttle = self.rightPower
