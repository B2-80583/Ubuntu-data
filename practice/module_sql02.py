import mysql.connector

# curser to locate and iterate the data

mydb = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'manager',
    database = 'classwork_db'
)

mycursor = mydb.cursor()
sql = 'select * from emp where job = %s'
val = ('analyst',) # it take only tuple or list othewise it will give error
mycursor.execute(sql, val)
result = mycursor.fetchall()
mycursor.close()

for x in result:
    print(x)
