dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={}
for i in (dict1,dict2):
    #print(i)
    dict3.update(i)
print(dict3)


