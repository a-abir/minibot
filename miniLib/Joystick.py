import pygame
pygame.init()

class Joystick:
    def __init__(self):
        pygame.Joystick.init()

    def info(self):
        jstickCount = pygame.joystick.get_count()
        print("Number of Joysticks connected: \n", jstickCount)
        # For each joystick:
        for i in range(jstickCount):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            print(f"Joystick {i}")
            # Get the name from the OS for the controller/joystick.
            print(f"Joystick name: {joystick.get_name()}")
            # Usually axis run in pairs, up/down for one, and left/right
            print(f"Number of axes: {joystick.get_numaxes()}")
            print(f"Number of buttons: {joystick.get_numbuttons()}")

    def newJoystick(self, id, _return=False):
        self.jstick = pygame.joystick.Joystick(id)
        self.jstick.init()
        if _return:
            return self.jstick

    def getAxis(self, axisID):
        return self.jstick.get_axis(axisID)

    def getButton(self, buttonID):
        return self.jstick.get_button(buttonID)