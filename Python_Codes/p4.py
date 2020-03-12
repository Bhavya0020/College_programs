def len(num):
    l=0
    # print(num)
    while (num >0):
        num//=10
        # print(num)
        l=l+1
    
    return l

def armstrong(num):
    s=0

    rem=0
    l=len(num)
    # print(l)
    # print(num)
    t=num
    p=10
    for i in range(0,l):
        rem=num%10
        num=num//10
        rem=rem**l
        s=s+rem
        # print(rem)
        p=p*10
    
    if(s == t):
        return True
    else:
        return False

def main():
    num = int(input("Enter a number"))
    # print(num)
    print(armstrong(num))


main()