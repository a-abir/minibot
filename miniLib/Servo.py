from setup import Servos, ContiniousServos

class Servo:
    def __init__(self, ID):
        self.servo = Servos[ID]

    def angle(self, degree):
        self.servo.angle = degree


class ContiniousServo:
    def __init__(self, ID):
        self.servo = ContiniousServos[ID]

    def throttle(self, power):
        self.servo.throttle = power
