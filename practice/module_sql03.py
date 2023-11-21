import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'manager',
    database = 'classwork_db'
)
mycursor = mydb.cursor()
sql = 'insert into emp(empno, ename, sal) values(%s, %s, %s)'
val = (1, "rohan", 1000)
mycursor.execute(sql, val)
result = mycursor.fetchall()
mycursor.close()
mydb.commit()

for x in result:
    print(x)