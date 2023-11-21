# Person =  age , name
# player = name and age , team

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(self.name)
        print(self.age)


class Player(Person):
    def __init__(self, name, age, team):
        Person.__init__(self, name, age)
        self.team = team


p1 = Person("person1", 20)
print(p1.__dict__)
p2 = Player("person2", 30, "india")
print(p2.__dict__)
