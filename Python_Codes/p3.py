
n=int(input("Enter The final term"))
sum=0
for i in range(1,n+1):
    sum+=i/(i+1)
    # print(i) print("/") print(i+1)

print("the sum of sequence is")
print(sum)