from iFeature import IFeature
from iCar import ICar


class Coloring(IFeature):

    def __init__(self, car: ICar):
        self.car = car

    def cost(self):
        return self.car.cost() + 1800

    def __str__(self):
        return f"Coloring - {self.car}"


class Insurance(IFeature):

    def __init__(self, car: ICar):
        self.car = car

    def cost(self):
        return self.car.cost() + 4800

    def __str__(self):
        return f"Insurance - {self.car}"
