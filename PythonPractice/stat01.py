import math

list_numbers = [45, 36, 40, 41, 41, 34, 39, 42, 41, 49, 36, 56, 38, 41, 38, 42, 40, 39]
# calculate range
large = max(list_numbers)
print(f"large = {large}")
small = min(list_numbers)
print(f"small = {small}")

range_numbers = large - small
print(f"Range of the data set = {range_numbers}")
print('-' * 100)
# calculate mean
sum = 0
for i in list_numbers:
    sum = sum + i
mean = sum / len(list_numbers)
print(f"mean = {mean}")
print('_' * 100)

list01 = []
for d in list_numbers:
    diff = round(d - mean, 2)
    list01.append(diff)
print(f"x - mean = {list01}")
print('_' * 100)

list02 = []
for s in list01:
    square = round(s * s, 2)
    list02.append(square)
print(f"(x - mean)^2 = {list02}")
print('_' * 100)

sum01 = 0
for square_sum in list02:
    sum01 = sum01 + square_sum

print(f"(x - mean)^2 sum = {sum01}")

standard_deviation = round(math.sqrt(sum01 / len(list_numbers)), 2)
print(f"standard deviation = {standard_deviation}")

var = round(standard_deviation ** 2, 2)
print(f"variance = {var}")
