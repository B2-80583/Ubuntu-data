# class person:
#     def __iter__(self, name):
#         self.__name = name
#
#     def __str__(self):
#         return f"person [name = {self.__name}]"


class Vehicle:
    def __init__(self, model):
        self._model = model

    def __str__(self):
        return f"Vehicle [name = {self._model}]"


class Car(Vehicle):
    def __init__(self, model, company):
        Vehicle.__init__(self, model)
        self._company = company

    def __str__(self):
        return f"car [model = {self._model}, company = {self._company}]"


c1 = Car("i10", "hyundai")
print(f"c1 = {c1}")
