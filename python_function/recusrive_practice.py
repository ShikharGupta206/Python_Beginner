# Sum of n numbers

def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)

print(sum(5))

# List elements

def ele(list,index=0):
    if(len(list)==index):
        return
    print(list[index])
    ele(list,index+1)
    
ele([3,4,5,6])