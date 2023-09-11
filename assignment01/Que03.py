# Write a program to accept a 4digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values If user
# enters a 4digit number 9361 output should be
# a. 9 3 6 1
# b. 9361 = 9 000 + 300 + 60 + 1
# c. 1639


user_input = input("Enter a number: ")
num = int(user_input)
# method 1 ------------------------------------------------------------------------
# part a -----------------------------------------------------------------------
for i in range(0, len(user_input)):
    # list1.append(user_input[i])
    print(f'{user_input[i]}', end=' ')

print('\n')

# part b -----------------------------------------------------------------------
print(f'{num} = ', end='')
for i in range(1, len(user_input)+1):
    # list1.append(user_input[i])
    new_num = int(user_input[-i]) * (10**(i-1))
    print(f'{new_num}', end=' + ')

print('\n')

# # part c -----------------------------------------------------------------------
# # string reversal using for loop
# for i in range(1, len(user_input) + 1):
#     print(user_input[-i])
# String reversal using string reverse/slicing { string_name[start:end:step] }
# doubt: string reversal with specified indices is not supported.
rev_num = user_input[::-1]
print(rev_num)





# method 2 ------------------------------------------------------------------------
# while num != 0:
#     digit = num % 10
#     num = num//10
#     print(digit)