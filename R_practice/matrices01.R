#matrices
# 
# m1 = matrix(c(10,20,30,40),nrow = 2,ncol = 2 )
# print(m1)
# m1 = matrix(c(10,20,30,40),nrow = 2,ncol = 2 ,byrow =1)
# print(m1)
# 
# m2 = matrix(1:12 *10,nrow =4,ncol=3)
# print(m2)
# m2 = matrix(1:12 *10,nrow =4,ncol=3,byrow=T)
# print(m2)
# 
# print(m2[1])
# print(m2[2,2])
# print(m2[,2])
# 
# print(m2[1,])
# print(m2[,2])
# print(m2[,3])
# print(m2[2,])
# 
# print(m2[1,2])
row.name = c('triber','i20','punch','figo','XUV')
col.name = c('model','company','price','mialage')
m3 = matrix(
  c(
   'triber', 'renault', 10.5, 18,
   'i20', 'hyundai', 12, 16,
   'punch', 'tata', 10, 20,
   'figo', 'ford', 8, 17,
   'XUV', 'mahindra', 21, 12),
    nrow = 5, ncol = 4, dimnames = list(row.name, col.name)
)

print(m3)
print(m3["XUV","mialage"])
 




