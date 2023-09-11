# Write a Python program to find given number is positive ,nigetive or zero

int_num = input("enter the number:")
num = int(int_num)

if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")
elif num == 0:
    print("number is zero")
else:
    print("invalid number")