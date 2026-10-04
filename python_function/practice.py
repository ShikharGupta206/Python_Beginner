# Lenght of a list

def lenght(list):
    l=len(list)
    print(l)

lenght([2,3,4,5])


# Elements of a list in single line

def ele(list):
    for i in list:
        print(i,end=" ")

ele([2,3,4,5,6,7])

# factorial of a number

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)

fact(5)

#  USd to INR
def INR(n):
    print(n*100)

INR(5)



