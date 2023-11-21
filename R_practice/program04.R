# # recycling of values
# m2 = matrix(c(10,20,30,40), nrow = 4, ncol = 4)
# print(m2)

# factors 

# colors.factor =factor(
#   c("red","white","yellow","black","red","pink","pink","red"),
#   levels = c("red","pink","black","yellow","white"),
#   labels = c(1,2,3,4,5))
# print(colors.factor)

models = c("i10","i20","swift","polo","breeza")
companies = c("hyundai","hyundai","suzuki","volksworgon","suzuki")
prices = c(12000,300000,400000,500000,5000000)

cars.df = data.frame(
  model = models,
  company = companies,
  price = prices
)
print(cars.df)
print(head(cars.df,3))
print(tail(cars.df,2))

print(nrow(cars.df))
print(ncol(cars.df))  

print(colnames(cars.df))
print(rownames(cars.df))
str(cars.df)

print(summary(cars.df))
print(typeof(cars.df))
View(cars.df)


print(cars.df$price)
print(cars.df$model)
print(cars.df$model[1])
