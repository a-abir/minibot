from adafruit_servokit import ServoKit

class Servo:
    def __init__(self):
        self.kit = ServoKit(channels=16)

    def newServo(self, pwmID):
        return kit.continuous_servo[pwmID]
