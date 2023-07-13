from singleton import Animal


if __name__ == '__main__':

    animal_01 = Animal()
    animal_02 = Animal()

    animal_01.name = 'Animal-01'

    print(animal_01 is animal_02)
    print(animal_02)
