f=open("story.txt","r")
c=0
for i in f:
	a=i.strip()
	list1=a.split()
	for j in list1:
		if j[-1]=="e":
			c+=1
print("count of words ending with e",c)