from parse import Servos, ContiniousServos

class Servo:
    def __init__(self, ID):
        '''
        Initialize a Servo

        :param ID: ID of the Servo [0,1,2,3]
        :type ID: int
        '''
        self.servo = Servos[ID]

    def angle(self, degree):
        '''
        Set the angle to rotate to

        :param degree: degree of the Servo
        :type degree: int
        '''
        self.servo.angle = degree


class ContiniousServo:
    def __init__(self, ID):
        '''
        Initialize a Continious Servo

        :param ID: ID of the Continious Servo [0,1,2,3]
        :type ID: int
        '''
        self.servo = ContiniousServos[ID]

    def throttle(self, power):
        '''
        Set the throttle of the Continious Servo

        :param power: Power of the Continious Servo -1 to 1
        :type power: float
        '''
        self.servo.throttle = power
