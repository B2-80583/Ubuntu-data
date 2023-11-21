class Car:
    def __init__(self, model, company):
        self.__model = model
        self.__company = company

    def print_car(self):
        print(self.__model)
        print(self.__company)


class Person:
    def __init__(self, name, age, car_model, car_company):
        self.__name = name
        self.__age = age
        self.__car = Car(car_model, car_company)  # object of car type

    def print_person(self):
        print(self.__name)
        print(self.__age)
        self.__car.print_car()
        print()


p1 = Person('rashmi', 18, "i10", "hyundai", )
p1.print_person()
