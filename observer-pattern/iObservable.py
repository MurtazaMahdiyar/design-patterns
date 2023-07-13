from abc import ABC, abstractmethod


class IObservable(ABC):

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def notify(self):
        pass
