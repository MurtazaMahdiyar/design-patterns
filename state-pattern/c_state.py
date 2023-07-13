from State import State

class Closed(State):    
    __gate = None

    def __init__(self, gate):
        self.gate = gate
        self.gate.ledColor = 'Red'

    def __str__(self):
        return 'Closed'

    def pay(self):
        self.gate.state = Process(self.gate)

    def payOk(self):
        pass

    def payFail(self):
        pass

    def enter(self):
        print('Beep!')

    @property
    def gate(self):
        return self.__gate

    @gate.setter
    def gate(self, gate):
        self.__gate = gate


class Process(State):
    __gate = None

    def __init__(self, gate):
        self.gate = gate
        self.gate.ledColor = 'Yellow'

    def __str__(self):
        return 'Process'

    def pay(self):
        print('Beep!')

    def payOk(self):
        self.gate.state = Open(self.gate)

    def payFail(self):
        self.gate.state = Closed(self.gate)

    def enter(self):
        print('Beep!')

    @property
    def gate(self):
        return self.__gate

    @gate.setter
    def gate(self, gate):
        self.__gate = gate


class Open(State):
    __gate = None

    def __init__(self, gate):
        self.gate = gate
        self.gate.ledColor = 'Green'

    def __str__(self):
        return 'Open'

    def pay(self):
        print('Beep!')

    def payOk(self):
        pass

    def payFail(self):
        pass

    def enter(self):
        self.gate.state = Closed(self.gate)

    @property
    def gate(self):
        return self.__gate

    @gate.setter
    def gate(self, gate):
        self.__gate = gate
