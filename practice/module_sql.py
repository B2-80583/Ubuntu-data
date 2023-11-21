import mysql.connector

# curser to locate and iterate the data

mydb = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'manager',
    database = 'classwork_db'
)

mycursor = mydb.cursor()
sql = 'select * from emp'
mycursor.execute(sql)
result = mycursor.fetchall()
mycursor.close()

for x in result:
    print(x)
