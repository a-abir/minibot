from miniLib import Joystick, ArcadeDrive, Motor

def main():
    left = Motor(0)
    right = Motor(1)

    jstick = Joystick(0)

    robot = ArcadeDrive(left, right)

    while True:
        forwardAxis = jstick.getAxis(1)
        steerAxis = jstick.getAxis(3)

        robot.drive(forwardAxis, steerAxis)

if __name__ == "__main__":
    main()
