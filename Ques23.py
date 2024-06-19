unit=input("enter unit of input temperature (F/C) : ")
inputT=int(input("enter temperature in "+ unit+" : "))
if(unit in " f F " ):
    outputT=(5/9)*(inputT-32)
    print(outputT," defree celcius")
elif(unit in " c C " ):
    outputT=((9/5)*inputT)+32 
    print(outputT,"fahrenheit")