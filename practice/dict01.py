# rashmi = dict()
# print(rashmi)
# rashmi['one'] = 1
# print(rashmi)
# rashmi = {'one': 1, 'two': 2, 'three': 3}
# print(type(rashmi))
# print(rashmi['two'])
# # print(rashmi['four']) if key is not present in the dict then it will return error
# print(len(rashmi))
# print('one' in rashmi)
# # print(1 in rashmi) method in not work with values
# # for value we have to use dict.values method convert it into list and the find for values
# rash = list(rashmi.values())
# print(1 in rash)


# counts the words in sentence
# with for loop and indexing in dict method
sentance = 'if key is not present in the dict then it will return error'
word = sentance.replace(" ", "")
print(word)
print("method 1")
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

# with dict.get function
r = dict()
print('method 2')
for i in word:
    r[i] = r.get(i,0) + 1
print(r)