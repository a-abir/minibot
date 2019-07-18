import pygame
pygame.init()

class Joystick:
    def __init__(self):
        '''
        Setup Joystick control using pygame
        '''
        pygame.joystick.init()

    def info(self):
        '''
        Print out info regarding all connected joystics
        '''
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
        '''
        Setup a new joystick

        :param id: ID of the joystick
        :type id: int
        :param _return: return joystick instance, defaults to False
        :type _return: bool, optional
        :return: joystick instance if _return == True
        :rtype: pygame.joystick.Joystick
        '''
        self.jstick = pygame.joystick.Joystick(id)
        self.jstick.init()
        if _return:
            return self.jstick

    def getAxis(self, axisID):
        '''
        Get the value of the axis

        :param axisID: Id of the axis
        :type axisID: int
        :return: value of the axis
        :rtype: float
        '''
        return self.jstick.get_axis(axisID)

    def getButton(self, buttonID):
        '''
        Get the state of the button

        :param buttonID: Id of the button
        :type buttonID: int
        :return: state of the button
        :rtype: bool
        '''
        return self.jstick.get_button(buttonID)
