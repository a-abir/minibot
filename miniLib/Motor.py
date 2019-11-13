from adafruit_crickit import crickit

class Motor:
    Motors = [crickit.dc_motor_1, crickit.dc_motor_2]
    def __init__(self, ID):
        '''
        Inintialize the DC Motor

        :param ID: The ID of the Motor [0,1]
        :type ID: int
        '''
        self.motor = self.Motors[ID]

    def throttle(self, power):
        '''
        Input power for the Motor

        :param power: Value from -1 to 1
        :type power: float
        '''
        self.motor.throttle = power
