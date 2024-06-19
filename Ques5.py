str = input("Enter string input : ")
fileobj=open("FileName.txt",'w')
print(str,file=fileobj)