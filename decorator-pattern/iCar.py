from abc import ABC, abstractmethod


class ICar(ABC):

    @abstractmethod
    def cost(self):
        pass
