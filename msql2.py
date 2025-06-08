import mysql.connector

mydb=mysql.connector.connect(
	host='localhost',
	user='root',
	password='root@123',
	database='db1')

mycursor=mydb.cursor()
Name=input("Enter name: ")
Address=input("Enter address: ")
sql="insert into employee(name,address) values(%s,%s)"
val=(Name,Address)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")