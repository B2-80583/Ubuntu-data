# # def function():
# #     persons_info = {'name' : 'rashmi', 'age': 18, 'address': 'pune'}
# #     if persons_info['age'] >= 18:
# #         print("eligible for voting")
# #     else:
# #         print("Not eligible")
#
#
# # create A CLASS named mobile to store mobile's data in terms
# # of model, company and price. create two objects to store two mobile's data
#
#
# class MobileData:
#     """this class will store mobile's information"""
#     pass
#
# m1= MobileData()
#
# setattr(m1,"model", "iphone 6+")
# setattr(m1,"company", "Apple")
# setattr(m1,"price", "120000")
#
#
# print(f"model = {getattr(m1,'model')}")
# print(f"company = {getattr(m1,'company')}")
# print(f"price= {getattr(m1,'price')}")
#
# m3 = MobileData()
#
# setattr(m3,"model", "iphone 6+")
# setattr(m3,"company", "Apple")
# setattr(m3,"price", "120000")
#
#
# print(f"model = {getattr(m3,'model')}")
# print(f"company = {getattr(m3,'company')}")
# print(f"price= {getattr(m3,'price')}")
#
#
#


 # create a class name car with model and company
 # create two functions
 #- set_car_data
 # - Print_car




class CarInfo:
    pass


def set_car_data(reference,model,company):
    setattr(reference, "model", model)
    setattr(reference,"company", company)

carinfo = CarInfo()


