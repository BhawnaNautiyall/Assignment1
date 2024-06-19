#remove punctuations
str2=""
str=input("enter String : ")
for s in str:
    if(s.isalnum() or s==" "):
        str2+=s
str=str2
print(str)