# v1 = c(T,F,T,F)
# v2 = c(F,T, T,F)
# print(v1 & v2)
# print(v1 | v2)
# # perform logical and operation on 1st value of v1 and true
# print(v1 && TRUE)
# # perform logical or operation
# print(v1 || TRUE)
# 
# numbers = c(10,20,30,40,50,60,70,80,90,100)
# 
# numbers = 1:10 * 10
# print(numbers)
# #slicing
# print(numbers[3:7])
# #print(numbers[:7])
# #print(numbers[3:])
# print(numbers[-1:-7])


#list
# l1 = list(
#  c(10,20,30,40,50),
#  c(60,70,80,90,100)
# )
# 
# print(l1)
# print(l1[[1]][[1]])
# print(l1[[1]][3])
# print(l1[[2]][4])
# 
# 
# list2 = list(
#   c(10,20,30,40,50),
#   c("india","USA","uk","japan"),
#   c(T,F),
#   c(15.50,50.60,30.50,80.70,90.10)
# )
# 
# print(list2[[1]])
# print(list2[[2]])
# print(list2[[3]])
# print(list2[[4]])
# print(list2[[1]][3])
# print(list2[[2]][4])
# print(list2[[3]][1])
# print(list2[[4]][3])
# print(list2[[4]][5])
# print(list2[[2]][2])

list04 = list(
  persons = c("person1","person2","person3"),
  cars = c("i20","figo","triber","XUV"),
  language = c("c","c++","Python","R","Java","JavaScript"),
  prime = c(1,2,3,5,7,11,13,17,19,21,23,29)
)

print(list04$persons)
print(list04$cars)
print(list04$language)
print(list04$prime)
print(list04$persons[3])
print(list04$cars[4])
print(list04$language[3])
print(list04$prime[9])
print(list04$prime[11])
print(list04$prime[4])









