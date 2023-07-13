from iCar import ICar
import random


class Hyundai(ICar):

    def __init__(self, name=f'hyundai-{random.randrange(1000, 2000)}'):
        self.reg_number = random.randint(1000000, 2000000)
        self.name = name

    def cost(self):
        return 178000

    def __str__(self):
        return f'{self.reg_number}: {self.name} - {self.cost()}'


class Ferrari(ICar):

    def __init__(self, name=f'ferrari-{random.randrange(1000, 2000)}'):
        self.reg_number = random.randint(1000000, 2000000)
        self.name = name

    def cost(self):
        return 230000
    
    def __str__(self):
        return f'{self.reg_number}: {self.name} - {self.cost()}'
