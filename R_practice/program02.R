# indexing

numbers = c(10,20,30,40,50,60,70,80,90,100)
cat("numbers[1]",numbers[1])
cat("numbers[2]",numbers[2])
cat("numbers[3]",numbers[3])
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])

print(numbers[c(1,2,3,4,5)])
print(numbers[c(-6,-7,-8,-9,-10)])
print(numbers[c(2,3,5,6)])
print(numbers[c(-1,-4,-7,-8,-9,-10)])
print(numbers[c(1,5,2,4,8,10)])
print(numbers[c(10,2,5,7,9)])


print(numbers[c(1,2,-5,-6)])
print(numbers[c(TRUE,TRUE,T,T,F,F,F,F,F,F)])
print(numbers[c(F,T,T,F,T,T,F,F,F,F)])


#mathmatical operations

numbers01 =c(1,5,2,3,6,7)
print(numbers01 + 5)
print(numbers01 * 5)

print(numbers01 / 5)

print(numbers01 == 5)
print(numbers01 <= 5)
print(numbers01 >= 5)
print(numbers01 < 5)
print(numbers01 > 5)







