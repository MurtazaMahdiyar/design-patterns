from concrete_cars import Hyundai, Ferrari
from features import Coloring, Insurance


if __name__ == '__main__':

    buyBasket = Coloring(Insurance(Hyundai()))

    print(buyBasket.cost())
    print(buyBasket)
