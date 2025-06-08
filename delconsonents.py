def delete_consonent(str1):
    t1=("a","e","i","o","u","A","E","I","O","U")
    str2=""
    for i in str1:
        if i in t1:
            str2=str2+i
    return str2
string1=input("Enter a string: ")
string2=delete_consonent(string1)
print("String without cosonents: ",string2)