name=input("enter file name")
f=open(name,"r")
for i in f:
	a=i.strip()
	list1=a.split()
	for i in list1:
		if "," in i:
			print(i)
			s=i.replace(","," ")
			print(s)

