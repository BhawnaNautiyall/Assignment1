fo1=open("FileName.txt",'r')
fo2=open("CopiedFile.txt",'w')


content = fo1.read()
fo2.write(content)