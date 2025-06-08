def display_words(f):
	for i in f:
		a=i.strip()
		list1=a.split()
		for j in list1:
			if len(j)<4:
				print(j)
f=open("story.txt","r")
display_words(f)