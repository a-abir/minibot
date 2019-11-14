import pygame

class Joystick:
    def __init__(self, ID, deadband=0):
        '''
        Setup Joystick control using pygame
        '''
        pygame.init()
        pygame.joystick.init()
        self.deadband = abs(deadband)
        self.newJoystick(ID)

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

            print("Joystick {}".format(i))
            # Get the name from the OS for the controller/joystick.
            print("Joystick name: {}".format(joystick.get_name()))
            # Usually axis run in pairs, up/down for one, and left/right
            print("Number of axes: {}".format(joystick.get_numaxes()))
            print("Number of buttons: {}".format(joystick.get_numbuttons()))

    def newJoystick(self, deviceID, _return=False):
        '''
        Setup a new joystick

        :param deviceID: ID of the joystick
        :type deviceID: int
        :param _return: return joystick instance, defaults to False
        :type _return: bool, optional
        :return: joystick instance if _return == True
        :rtype: pygame.joystick.Joystick
        '''
        self.jstick = pygame.joystick.Joystick(deviceID)
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
        pygame.event.pump()
        _return = self.jstick.get_axis(axisID) if self.jstick.get_axis(axisID) > self.deadband or self.jstick.get_axis(axisID) < -self.deadband else 0
        return _return

    def getButton(self, buttonID):
        '''
        Get the state of the button

        :param buttonID: Id of the button
        :type buttonID: int
        :return: state of the button
        :rtype: bool
        '''
        return self.jstick.get_button(buttonID)
