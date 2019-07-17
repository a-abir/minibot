from miniLib import ArcadeDrive, Servo, Joystick

servo = Servo()
leftServo = servo.newServo(0)
rightServo = servo.newServo(1)

jstick = Joystick()
jstick.info()
jstick.newJoystick(0)

drive = ArcadeDrive(leftServo, rightServo)
while True:
    forwardAxis = jstick.getAxis(1)
    steerAxis = jstick.getAxis(3)
    drive.drive(forwardAxis, steerAxis)
