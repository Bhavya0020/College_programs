# Create List Of Auto Parts Along with Name & Price...

a=[]
n=int(input("Enter the number of elements in list : "))
for i in range(n):
    b=input("Enter name and price of product")
    a.append(b.split())

for i in a:
    print(i)