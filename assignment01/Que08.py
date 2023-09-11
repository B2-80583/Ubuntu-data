# Write a program that prompts the user to input number of calls and
# calculate the monthly telephone bills
# as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls

int_num = input("enter the number of calls:")
no_of_calls = int(int_num)
if no_of_calls <= 100:
    print(f"the bill will be = {200}")
if no_of_calls > 100 & no_of_calls <= 150 :
    print(f"the bill will be = {200+(0.60*50)}")
if no_of_calls > 150 & no_of_calls <= 200:
    print(f"the bill will be = { 200+(0.60*50)+(0.50*50)}")
if no_of_calls > 200:
    print(f"the bill will be = {no_of_calls * 0.40}")