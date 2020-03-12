n=int(input())
filename="students.txt"
file=open(filename,"w")
for i in range(0,n):
    name=str(input())
    rno=str(input())
    line=[name," ",rno,"\n"]
    file.writelines(line)

file.close()
file2=open(filename,"r")
line=file2.read()
print(line)
file2.close()