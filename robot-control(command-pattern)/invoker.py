from abc import ABC, abstractmethod


class Invoker(ABC):
    pass

    @abstractmethod
    def setCommand(self, command_name):
        pass

    @abstractmethod
    def unsetCommand(self, command_name):
        pass

    @abstractmethod
    def runCommand(self, command_name):
        pass
