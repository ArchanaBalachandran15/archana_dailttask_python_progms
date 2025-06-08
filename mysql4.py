import mysql.connector

mydb=mysql.connector.connect(
	host='localhost',
	user='root',
	password='root@123',
	database='db1')

mycursor=mydb.cursor()
#createsql="CREATE TABLE contactbook(Name varchar(10), Phoneno bigint)"
#mycursor.execute(createsql)
while(True):
	print("1. Insertion")
	print("2. Updation")
	print("3. Deletion")
	print("4. Display")
	print("5. Exit")
	n=int(input("Enter option: "))
	if n==1:
		n=input("Enter name: ")
		mycursor.execute("select name from contactbook")
		namelist=mycursor.fetchall()
		f=0
		for i in range(len(namelist)):
			if namelist[i][0]==n:
				f=1
				break
		if f==1:
			print("Contact",n," already exist")
		else:				
			num=int(input("Enter number: "))
			mycursor.execute("insert into contactbook(Name,Phoneno) values(%s,%s)",(n,num))
			mydb.commit()
			print("SUCCESS")
	elif n==2:
		print("1. Update Name")
		print("2. Update Number")
		mycursor.execute("select name from contactbook")
		namelist=mycursor.fetchall()
		c=int(input("Enter choice: "))
		if c==1:
			oldname=input("Enter name: ")
			f=0
			for i in range(len(namelist)):
				if namelist[i][0]==oldname:
					f=1
					break
			if f==1:
				newname=input("Enter new name: ")
				t=0
				for i in range(len(namelist)):
					if namelist[i][0]==newname:
						t=1
						break
				if t==1:
					print("Name",newname,"already exist")
				else:
					mycursor.execute("update contactbook set Name=%s where Name=%s",(newname,oldname)) 
					mydb.commit()
					print("Name",oldname," updated to ",newname)
			else:
				print("Name",oldname," not exist")
		elif c==2:
			name=input("Enter name: ")
			s=0
			for i in range(len(namelist)):
				if namelist[i][0]==name:
					s=1
					break
			if s==1:
				num=int(input("Enter number: "))
				mycursor.execute("update contactbook set Phoneno=%s where Name=%s",(num,name))
				mydb.commit()
				print("Number of ",name," is updated to ",num)
			else:
				print("Contact ",name," not exist")
		else:
			print("Invalid choice!!")					
	elif n==3:
		name=input("Enter name to delete: ")
		mycursor.execute("select name from contactbook")
		namelist=mycursor.fetchall()
		r=0
		for i in range(len(namelist)):
			if namelist[i][0]==name:
				r=1
				break
		if r==1:
			mycursor.execute("delete from contactbook where Name=%s",(name,))
			mydb.commit()
			print("Contact ",name," deleted")
		else:
			print("Name ",name," not exist!!")
	elif n==4:
		mycursor.execute("select * from contactbook order by Name")
		data=mycursor.fetchall()
		print("Contacts")
		for i in range(len(data)):
			print(data[i][0],"  ",data[i][1])
	elif n==5:
		exit()
	else:
		print("Please Enter correct option!!")