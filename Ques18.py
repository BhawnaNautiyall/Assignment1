str1=input("enter string 1 :")
str2=input("enter string 2 :")

dic={}
for s in str1:
    if s in dic:
        dic[s]+=1
    else : 
        dic[s]=1
dic2={}
for s in str2:
    if s in dic2:
        dic2[s]+=1
    else : 
        dic2[s]=1

if(dic==dic2):
    print(True)
else:
    print(False)

