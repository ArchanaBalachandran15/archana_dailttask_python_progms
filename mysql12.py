import mysql.connector

mydb=mysql.connector.connect(
	host='localhost',
	user='root',
	password='root@123',
	database='db1')
mycursor=mydb.cursor()
query="CREATE TABLE employee(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(10), address VARCHAR(50))"
mycursor.execute(query)