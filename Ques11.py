#FIBONACCI SEQUENCE 
def fib(num):
    if(num==2):
        return 1
    elif(num==1):
        return 0
    return fib(num-1)+fib(num-2)

num=int(input("enter the term to print : "))

print("fibonacci series for",num,"terms : ")
for i in range(1,num+1):
    print(fib(i))
    
    