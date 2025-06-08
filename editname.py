def edit(str1):
    str2=str1.split(" ")
    str3=[]
    if len(str2)>=3:
        for i in range(2):
            str3.append(str2[i][0])
        str3.extend(str2[2:])
        for j in range(len(str3)):
            str3[j]=str3[j].capitalize()
        return (" ".join(str3))
    elif len(str2)==2:
        for i in range(1):
            str3.append(str2[i][0])
        str3.extend(str2[1:])
        for j in range(len(str3)):
            str3[j]=str3[j].capitalize()
        r=" ".join(str3)
        return r
    else:
        str3.extend(str1.capitalize())
        return("".join(str3))     