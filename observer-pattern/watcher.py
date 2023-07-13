from iObserver import IObserver
import random


class Watcher(IObserver):

    def __init__(self, name):
        self.id = random.randint(1000000, 2000000)
        self.name = name

    def update(self, data):
        print(f"{self.id} ({self.name}) : {data}")
