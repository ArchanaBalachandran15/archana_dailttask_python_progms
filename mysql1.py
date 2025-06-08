import mysql.connector

mydb=mysql.connector.connect(
	host='localhost',
	user='root',
	password='root@123')
mycursor=mydb.cursor()
query="create database db1"
mycursor.execute(query)