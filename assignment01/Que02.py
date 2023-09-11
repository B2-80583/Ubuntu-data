# Write a Python Program to Convert Celsius To Fahrenheit vice versa.
# fahrenheit = (celsius * 1.8) + 32
int_temp = input("enter the temprature  :")
temp = int(int_temp)
fahrenherit = (temp * 1.8) + 32
print(f"tempreture in fahrenherit : {fahrenherit}")
celsius = (fahrenherit - 32)/ 1.8
print(f"temprerature in celsius : {celsius}")