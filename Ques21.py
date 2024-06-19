str=input("enter string : ")
specialChar=input("enter character to count occurancce : ")
count=0

for s in str:
    if(s==specialChar):
        count+=1
print(specialChar, "occured " ,count,"times")