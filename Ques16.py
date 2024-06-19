dic={}
str=input("enter string : ")
for s in str:
    if s in dic:
        dic[s]+=1
    else : 
        dic[s]=1

print(dic)