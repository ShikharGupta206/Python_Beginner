# Printing Numbers
i=100
while(i>=1):
    print(i)
    i=i-1

# Multiplication
num=int(input("Enter the number"))
i=1
while(i<=10):
    print(i*num)
    i=i+1

# printing elements
list=[1,4,9,16,25,36,49,64,81,100]
n=len(list)
i=0
while(i<n):
    print(list[i])
    i=i+1

# Searching for a number
list=[1,4,9,16,25,36,49,64,81,100]
x=int(input("Enter the number"))
i=0
while(i<len(list)):
    if(list[i]==x):
        print("found at index :",i)
        break;
    i=i+1
else:
    print("Not found")


