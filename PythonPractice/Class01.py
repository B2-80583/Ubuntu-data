# class Person:
#     pass
#
#     def set_person_data(ref,name,age):
#         setattr(ref,"name",name)
#         setattr(ref, "age", age)
#
#     def print_person_data(ref):
#         print(f"name:{getattr(ref,'name')}")
#         print(f"age:{getattr(ref,'age')}")
#
# p1 = Person()
# p1.set_person_data('rashmi', 18)
# p1.print_person_data()


# class Car:
#     def __init__(self,model,company):
#         setattr(self,"model",model)
#         setattr(self,"company", company)
#     def print_car_details(self):
#         print(f"model = {getattr(self,'model')}")
#         print(f"company = {getattr(self,'company')}")
#
# c1 = Car("ghvjv","vijb")
# c1.print_car_details()


# create an employee class with
# - attrs = empolyee_id, name, salary
# - methods = initializer, print_details


# class Employee:
#     def __init__(self, employee_id=0, name="", salary=0):
#         setattr(self, "employee_id", employee_id)
#         setattr(self, "name", name)
#         setattr(self, "salary", salary)
#
#     # facilitator
#     def print_details(self):
#         print(f"employee_id = {getattr(self, 'employee_id')}")
#         print(f"employee_id = {getattr(self, 'name')}")
#         print(f"employee_id = {getattr(self, 'salary')}")
#
#
# E1 = Employee(34216, "rashmi", 2521)
# # E1 = Employee()
# E1.print_details()
#

# create a student calls with
# attributes = roll_no, name, marks
# methods = initializer, print_details, setter, getter


# class Student:
#     def __init__(self, roll_no=0, name="", marks=0):
#         setattr(self, "roll_no", roll_no)
#         setattr(self, "name", name)
#         setattr(self, "marks", marks)
#
#     def print_details(self):
#         print(f"roll_no = {getattr(self, 'roll_no')}")
#         print(f"name = {getattr(self, 'name')}")
#         print(f"marks = {getattr(self, 'marks')}")
#
#     def set_roll_no(self, roll_no):
#         setattr(self, "age", roll_no)
#
#     def get_roll_no(self):
#         return getattr(self, "roll_no")
#
# s1 = Student()
# # s1.print_details()
# s1.set_roll_no(123)
# s1.get_roll_no()

# setter and getter
class School:
    def __init__(self, name, address, student_count):
        self.name = name
        self.address = address
        self.student_count = student_count

    def print_details(self):
        print(self.name)
        print(self.address)
        print(self.student_count)


s1 = School("school1","pune",1321)
s1.print_details()
