str1=input("enter string : ")
str2=input("enter substring : ")

if(str1.startswith(str2) or str1.endswith(str2)):
    print(True)
else:
    print(False)