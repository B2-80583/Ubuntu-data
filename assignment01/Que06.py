# Write a Python Program Get age input from user and check if user is eligible for voting
int_age = input("enter the age of the person:")
age = int(int_age)
if age >= 18:
    print("person is eligible for voting")
else:
    print("not eligible for voting")