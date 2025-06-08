f=open("story.txt","r")
d=f.read()
c=0
for i in d:
	if i.isupper():
		c=c+1
print("count of upper case characters: ",c)