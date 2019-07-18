from adafruit_servokit import ServoKit

class Servo:
    def __init__(self):
        '''
        Setup servo for using adafruit servokit
        '''
        self.kit = ServoKit(channels=16)

    def newServo(self, pwmID):
        '''
        Setup a servo given pwm ID

        :param pwmID: ID of the servo
        :type pwmID: int
        :return: instance of continuous servo
        :rtype: continuous_servo
        '''
        return kit.continuous_servo[pwmID]
