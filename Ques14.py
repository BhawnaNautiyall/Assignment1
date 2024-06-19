lines=""
i=1
while(True):
    str1=input("enter line "+str(i)+" : ")
    i+=1
    lines+="\n"+str1
    if(str1==""):
        break
print(lines)