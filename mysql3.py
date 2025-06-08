import mysql.connector

mydb=mysql.connector.connect(
	host='localhost',
	user='root',
	password='root@123',
	database='db1')

mycursor=mydb.cursor()
#mycursor.execute("select * from employee")
#list1=mycursor.fetchall()
#print(list1)
#print(type(list1))
#for i in list1:
#    print(i)

#Name=input("Enter name: ")
#sql="select * from employee where name=(%s)"
#mycursor.execute(sql,(Name,))
#mycursor.execute("select name from employee")
#mycursor.execute("select * from employee where name='ADE'")
#list1=mycursor.fetchall()
#print(list1)
#mycursor.execute("select * from employee order by name desc")
#mycursor.execute("select name from employee order by name")
#l1=mycursor.fetchall()
#print(l1)

#to fetch one record
#myresult=mycursor.fetchone()
#print(myresult)



#delete
#name=input("enter name:")
#mycursor.execute("delete from employee where name=%s",(name,))
#mydb.commit()



#update
#newname=input("enter new name: ")
#oldname=input("enter old name: ")
#mycursor.execute("update employee set name=%s where name=%s",(newname,oldname))
#mydb.commit()