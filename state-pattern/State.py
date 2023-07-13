from abc import ABC, abstractmethod

class State(ABC):
    
    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def payOk(self):
        pass
    
    @abstractmethod
    def payFail(self):
        pass

    @abstractmethod
    def enter(self):
        pass
