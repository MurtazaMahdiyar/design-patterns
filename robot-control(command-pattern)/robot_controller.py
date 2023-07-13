from concrete_commands import MoveRight
from invoker import Invoker
from iCommand import ICommand
from robot import Robot


class RobotController(Invoker):
    __commands: ICommand = []
    __stack: ICommand = []

    def __init__(self, robot: Robot):
        self.robot = robot

    def setCommand(self, command):
        if isinstance(command, ICommand):
            self.__commands.append(command)

    def unsetCommand(self, command):
        if isinstance(command, ICommand):
            self.__commands.remove(command)

    def runCommand(self, command: ICommand, undo=False):
        if command in self.__commands:
            if undo == False:
                command.execute(self.robot)
                self.__stack.append(command)
            else:
                command.unexecute(self.robot)

    def undoCommand(self):
        if self.__stack != []:
            self.runCommand(self.__stack.pop(), undo=True)
