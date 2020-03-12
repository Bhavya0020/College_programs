

def GCD(x,y):

    if x>y:
        small = y
    else:
        small = x
    
    for i in range(1,small+1):
        if((x%i==0) and (y%i==0)):
            gcd=i

    return gcd

x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))

print(GCD(x,y))