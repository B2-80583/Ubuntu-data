# Write a Python function to find the maximum of three numbers.

int_num01 = input("enter the value of first:")
num01 = int(int_num01)
int_num02 = input("enter the value of second:")
num02 = int(int_num02)
int_num03 = input("enter the value of third:")
num03 = int(int_num03)

if num01 > num02 & num01 > num03:
    print(f"{num01} is the greatest")
elif num02 > num01 & num02 > num03:
    print(f"{num02} is the greatest")
else:
    print(f"{num03} is the greatest")

# not taking float and not taking int non base 10 values