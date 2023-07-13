from abc import ABC, abstractmethod
from formElement.WindowsFormElement import *
from formElement.LinuxFormElement import *
from formElement.MacFormElement import *


class FormFactory(ABC):

    @abstractmethod
    def desc(self):
        pass

    @abstractmethod
    def getInput(self):
        pass

    @abstractmethod
    def getButton(self):
        pass

    @abstractmethod
    def getAlert(self):
        pass


class WindowsFormFactory(FormFactory):

    def desc(self):
        print('Windows compatible ui form.')

    def getInput(self):
        return WinFormInput()

    def getAlert(self):
        return WinFormAlert()

    def getButton(self):
        return WinFormButton()


class LinuxFormFactory(FormFactory):

    def desc(self):
        print("Linux compatible ui form.")

    def getInput(self):
        return LinuxFormInput()

    def getAlert(self):
        return LinuxFormAlert()

    def getButton(self):
        return LinuxFormButton()


class MacOSFormFactory(FormFactory):

    def desc(self):
        print("MacOS compatible ui form.")

    def getInput(self):
        return MacFormInput()

    def getAlert(self):
        return MacFormAlert()

    def getButton(self):
        return MacFormButton()
