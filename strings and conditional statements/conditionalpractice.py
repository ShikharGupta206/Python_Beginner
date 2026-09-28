# program 1
num=int(input("Enter the number"))
if(num%2==0):
    print("even")
else:
    print("odd")

# program 2
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
num3=int(input("Enter the number"))
if(num1==num2==num3):
    print("All are equal")
else:
    if(num1>=num2 and num1>=num3):
        print(num1)
    elif(num2>=num3 and num2>=num1):
        print(num2)
    else:
        print(num3)

# program 3
n=int(input("Enter the number"))
if(n%7==0):
    print("Yes")
else:
    print("no")