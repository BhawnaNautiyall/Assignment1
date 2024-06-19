num1=int(input("enter 1st number for operation : "))
op=input("which operation do you want to perform (+-*/) ? :")
num2=int(input("enter 2nd number for operation : "))

if(op in " + "):
    print(num1+num2)
elif(op in " * "):
    print(num1*num2)
elif(op in " - "):
    print(num1-num2)
elif(op in " / "):
    print(num1/num2)
else :
    print("wrong inputs")