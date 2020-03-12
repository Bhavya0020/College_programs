
def main():
    print("Enter the number of records")
    n=int(input())
    d={}
    for i in range(0,n):
        print("Enter name of pet")
        name=str(input())
        print("Enter type of pet")
        pet=str(input())
        d[name]=pet
    print("Enter the name of pet to be searched..")
    s=str(input())
    print(d[s])

main()