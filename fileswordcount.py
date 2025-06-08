f=open("story.txt","r")
t,c=0,0
l=1
for i in f:
	'''
	i.count("the")
	print(c)
	'''
	list1=i.split(" ")
	c=list1.count("the")
	t=t+c
	#print("line",l,"-",c)
	l+=1
print("total count is: ",t)
f.close()