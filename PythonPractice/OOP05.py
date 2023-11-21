# car is composed of engine
# class Engin: type, cc
# class Car : model, company

class Engin:
    def __init__(self, type, cc):
        self.__type = type
        self.__cc = cc

    def print_engin(self):
        print(self.__type)
        print(self.__cc)


class Car:
    def __init__(self, model, company, engin_type, engin_cc):
        self.__model = model
        self.__company = company
        self.__engin = Engin(engin_type, engin_cc)

    def print_car(self):
        print(self.__model)
        print(self.__company)
        self.__engin.print_engin()
        print()

c1 = Car('i10','hyundai','petrol', '5000')
c1.print_car()
