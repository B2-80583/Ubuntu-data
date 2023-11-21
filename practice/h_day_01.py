fruit = 'banana'
# index = len(fruit)
# while index > 0:
#     letter = fruit[index-1]
#     index = index - 1
#     print(f"{letter}", end=" ")
#
# print(fruit[:])
# def count(word, l):
#     count = 0
#     for letter in word:
#         if l == letter:
#             count = count + 1
#     print(f"count of letter {l}: {count}")
#
#
# count('banana', 'b')

# print(fruit.count("a"))
#
# c = 42
# print('%d' % c)
#
#
# numbers = [10, 20, 30, 40, 50]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
#     print(numbers[i])

#
# total = 0
# count = 0
# while (True):
#     inp = float(input("enter a number:"))
#     end = 0
#     if inp == end:
#         break
#     total = total + inp
#     count = count + 1
#
# average = total / count
#
# print(f"average : {average}")

#
# numbers = []
# while True:
#     inp = float(input("enter a number: "))
#     if inp == 0:
#         break
#     numbers.append(inp)
# average = sum(numbers)/len(numbers)
# print(f" average : {average}")


# s = 'spam_spam_spam'
# print(s)
# t = s.split('_')
# print(t)
# r = '_'.join(t)
# print(r)
#
#
# dict01 = dict()
# dict01['one'] = 'uno'
# print(dict01)
#

txt = 'but soft what light in yonder window breaks'
words = txt.split()
print(words)
t = []
for word in words:
    t.append([len(word), word])
print(t)
t.sort(reverse=True)
print(t)

res = []
len = []
for length, word in t:
    res.append(word)
    len.append(length)
print(res)
print(len)

