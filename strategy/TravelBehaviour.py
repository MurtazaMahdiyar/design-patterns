from abc import ABC, abstractmethod


class iTravelBehaviour(ABC):
    @abstractmethod
    def travel(self):
        pass


class TravelByCar(iTravelBehaviour):
    def travel(self):
        print("Travel by Car.")


class TravelByTrain(iTravelBehaviour):
    def travel(self):
        print("Travel by Train.")


class TravelByAirplane(iTravelBehaviour):
    def travel(self):
        print("Travel by Airplane")
