from abc import ABC, abstractmethod
from robot import Robot


class ICommand(ABC):

    @abstractmethod
    def execute(self, robot: Robot):
        pass

    @abstractmethod
    def unexecute(self, robot: Robot):
        pass
