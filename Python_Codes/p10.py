file1=open("students.txt","r")
file2=open("students2.txt","r")
file3=open("newfile.txt","w")
line=file1.read()
file3.write(line)
line2=file2.read()
file3.write(line2)
