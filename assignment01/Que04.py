# Write a program to accept three integer numbers and find its average.

int_num01 = input("enter the value of first:")
num01 = int(int_num01)
int_num02 = input("enter the value of second:")
num02 = int(int_num02)
int_num03 = input("enter the value of third:")
num03 = int(int_num03)

avg = (num01+num02+num03)/3
print(f"avarage of numbers: {avg}, type= {type(avg)}")

# avg is not declare still it is taking float by default