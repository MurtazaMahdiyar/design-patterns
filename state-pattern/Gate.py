from State import State
from c_state import *
from random import randint


class Gate:

    __id: int
    __ledColor: str
    __state: State = None

    def __init__(self):
        self.__state = Closed(self)
        self.ledColor = 'Red'
        self.__id = randint(1000000, 2000000)

    def __str__(self):
        return f'{self.__id}: {self.__state} ({self.ledColor})'

    def pay(self):
        self.state.pay()

    def payOk(self):
        self.state.payOk()

    def payFail(self):
        self.state.payFail()

    def enter(self):
        self.state.enter()

    # getters and setters

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, state):
        self.__state = state
        print(f'State changed!\n{self}')

    @property
    def ledColor(self):
        return self.__ledColor
    
    @ledColor.setter
    def ledColor(self, ledColor: str):
        self.__ledColor = ledColor
