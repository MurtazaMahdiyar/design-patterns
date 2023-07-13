from Person import Student, Politician, TaxiDriver
from TravelBehaviour import *


if __name__ == '__main__':

    student_01 = Student("Ali", 25)
    student_01.travelBehaviour = TravelByAirplane()
    student_01.performTravel()
    student_01.travelBehaviour = TravelByCar()
    student_01.performTravel()
    userChoice = int(input())

    match userChoice:
        case 1:
            student_01.travelBehaviour = TravelByAirplane()
        case 2:
            student_01.travelBehaviour = TravelByTrain()
        case _:
            student_01.travelBehaviour = TravelByCar()

    print("-----------------------")
    print("After user-select")
    student_01.performTravel()
