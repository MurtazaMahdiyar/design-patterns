import random


class Animal:

    def __init__(self):
        self.id = random.randint(1000, 2000)
        self.name = 'anonymous'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Animal, cls).__new__(cls)
        return cls.instance

    def __str__(self):
        return f'{self.id}: {self.name}'
