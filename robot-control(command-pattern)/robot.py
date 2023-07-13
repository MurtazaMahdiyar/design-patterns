import random


class Robot:

    def __init__(self, name="anonymous"):
        self.name = name
        self.id = random.randint(1000000, 2000000)

    def __str__(self):
        return f"{self.id}: {self.name}"
