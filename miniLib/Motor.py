from setup import Motors

class Motor:
    def __init__(self, ID):
        self.motor = Motors[ID]

    def throttle(self, power):
        self.motor.throttle = power
