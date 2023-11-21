# write a class named computer
# attributes: model, company, price, cpu, ram, storage
# methods: initializer, setter, getter, print_info, is-affordable(40k)

class Computer:
    def __init__ (self, model, company, price, cpu, ram, storage):
        self.__model = model
        self.__company = company
        self.__price = price
        self.__cpu = cpu
        self.__ram = ram
        self.__storage = storage

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_company(self, company):
        self.__company = company

    def get_company(self):
        return self.__company

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_cpu(self):
        return self.__cpu

    def set_ram(self, ram):
        self.__ram = ram

    def get_ram(self):
        return self.__ram

    def set_storage(self, storage):
        self.__storage = storage

    def get_storage(self):
        return self.__storage


    def print_info(self):
        print(self.__model)
        print(self.__company)
        print(self.__price)
        print(self.__cpu)
        print(self.__ram)
        print(self.__storage)


    def id_afforadable(self):
        if self.__price >= 40000:
           print("affordable")
        else:
           print("NOT affordable")


