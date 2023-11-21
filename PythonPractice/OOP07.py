# create a class named vehicle
# override __str__ for converting object to string with value "vehicle[name= ""]"

# class Vehicle:
#     def __init__(self, model, company):
#         self.model = model
#         self.company = company
#
#
# class Car(Vehicle):
#     def __init__(self, name, model, company):
#         Vehicle.__init__(self, model, company)
#         self.company = company
#
#
# v1 = Vehicle("i10", "hyundai")


class Number:
     def __init__(self, num):
         self.__num = num

     def __str__(self):
         return f" Number[num = {self.__num}]"

     def __add__(self, other):
         return Number(self.__num + other.__num)

     def __sub__(self, other):
         return Number(self.__num - other.__num)

     def __mul__(self, other):
         return Number(self.__num * other.__num)

     def __truediv__(self, other):
        return Number(self.__num / other.__num)

     def __floordiv__(self, other):
         return Number(self.__num // other.__num)

     def __pow__(self, other):
         return Number(self.__num ** other.__num)

     def __lt__(self, other):
         return Number(self.__num < other.__num)

     def __gt__(self, other):
         return Number(self.__num > other.__num)

     def __eq__(self, other):
         return Number(self.__num == other.__num)

     def __neg__(self):
        return Number(self.__num != other.__num)

     def __ge__(self, other):
         return Number(self.__num >= other.__num)

     def __le__(self, other):
         return Number(self.__num <= other.__num)





n1 = Number(10)
n2 = Number(20)
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
print(f"{n1} / {n2} = {n1 / n2}")
print(f"{n1} // {n2} = {n1 // n2}")
print(f"{n1} ** {n2} = {n1 ** n2}")
print(f"{n1} < {n2} = {n1 < n2}")
print(f"{n1} > {n2} = {n1 > n2}")
print(f"{n1} == {n2} = {n1 == n2}")
print(f"{n1} != {n2} = {n1 != n2}")
print(f"{n1} >= {n2} = {n1 >= n2}")
print(f"{n1} <= {n2} = {n1 <= n2}")









