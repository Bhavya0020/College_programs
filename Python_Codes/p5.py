def ASCII_CHAR(num):
    print(chr(num))

def CHAR_ASCII(num):
    print(ord(num))

def main():
    print("what do u want to do.....")
    print("1. Convert Character to ASCII")
    print("2. Convert ASCII to Character")
    s=int(input(" "))
    if(s==1):
        num=int(input("Enter the number.."))
        ASCII_CHAR(num)
    elif(s==2):
        num=(input("Enter a character.."))
        CHAR_ASCII(num)
main()