def getSum(num):
    sum=0
    while(num>0):
        sum=sum+num%10
        num//=10
    return sum

def main():
    num=int(input("Enter a number"))
    print("sum of the digits is..")
    print(getSum(num))

main()