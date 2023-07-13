from abc import ABC, abstractmethod
from TravelBehaviour import iTravelBehaviour


class Person(ABC):
    __travelBehaviour: iTravelBehaviour

    @property
    def travelBehaviour(self):
        return self.__travelBehaviour

    @travelBehaviour.setter
    def travelBehaviour(self, value):
        if isinstance(value, iTravelBehaviour):
            self.__travelBehaviour = value

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def performTravel(self):
        self.travelBehaviour.travel()

    @abstractmethod
    def info():
        pass


class Student(Person):

    def info(self):
        print(f"Student - {self.name}, age: {self.age}")


class TaxiDriver(Person):
    def info(self):
        print(f"Taxi Driver - {self.name}, age: {self.age}")


class Politician(Person):
    def info(self):
        print(f"Politician - {self.name}, age: {self.age}")
