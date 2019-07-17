class ArcadeDrive:
    def __init__(self, LeftServo, rightServo):

        self.right = rightServo
        self.left = LeftServo

    def calculate(self, forward, steer):
        # calculate left and right power
        leftPower = forward + steer
        rightPower = forward - steer
        return leftPower, rightPower

    def drive(self, forwardAxis, steerAxis):
        self.leftPower, self.rightPower = self.calculate(forwardAxis, steerAxis)
        self.left.throttle = self.leftPower
        self.right.throttle = self.rightPower

