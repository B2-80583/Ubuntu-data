# class person:
#     pass
#
#
# p1 = person()
#
# setattr(p1, "name", "person1")
# setattr(p1, "address", "pune")
# setattr(p1, "email", "person1@test.com")
# setattr(p1, "age", 20)
#
# print(f"name = {getattr(p1,'name')}")
# print(f"address = {getattr(p1,'address')}")
# print(f"email = {getattr(p1,'email')}")
# print(f"age = {getattr(p1,'age')}")


# class mobile:
#     pass
#
#
# def print_mobileinfo(m):
#     print(f"model = {getattr(m, 'model')}")
#     print(f"company = {getattr(m, 'company')}")
#
#
# m1 = mobile()
#
# setattr(m1, "model", "iphone")
# setattr(m1, "company", "apple")
#
# print_mobileinfo(m1)


class Person:
    pass


def __init__(self, name="", company=""):
    setattr(self, "name", name)
    setattr(self, "company", company)


def persons_info(reference, name, address, age):
    setattr(reference, "name", name)
    setattr(reference, "address", address)
    setattr(reference, "age", age)


def print_persons_info(reference):
    print(f"name = {getattr(reference, 'name')}")
    print(f"address = {getattr(reference, 'address')}")
    print(f"age = {getattr(reference, 'age')}")


p1 = Person()
persons_info(p1, "rashmi", "pune", 18)
print_persons_info(p1)
