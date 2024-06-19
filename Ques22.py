n=int(input("enter how many numbers you wants to enter : "))
max=int(input("enter number : "))
for i in range(1,n):
    num=int(input("enter number : "))
    if(num>max):
        max=num
   
print("max number is : " ,max)