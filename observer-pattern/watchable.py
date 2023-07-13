from iObservable import IObservable
from iObserver import IObserver


class Watchable(IObservable):
    __observers: IObserver = []
    __data: str

    def __init__(self, data=''):
        self.data = data

    @property
    def observers(self):
        return self.__observers

    @observers.setter
    def observers(self, value):
        if isinstance(value, IObserver):
            self.__observers.append(value)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
        self.notify()

    def add(self, item):
        self.observers = item

    def remove(self, item):
        if item in self.observers:
            self.observers.remove(item)

    def notify(self):
        for observer in self.observers:
            observer.update(self.data)
