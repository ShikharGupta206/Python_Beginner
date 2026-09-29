# # Program 1

m1=input("Enter the name of the first movie:")
m2=input("Enter the name of the second movie:")
m3=input("Enter the name of the third movie:")

l=[]
l.append(m1)
l.append(m2)
l.append(m3)

print(l)

# program 2
list2=[1,2,3,2,1]
list3=[1,"abc","abc",1]
copy1=list2
copy2=list3
list2.reverse()
list3.reverse()
if(list2==copy1):
    print("Palindrome")
else:
    print("Not Palindrome")

if(list3==copy2):
    print("Palindrome")
else:print("Not palindrome")

# Program 3

tup1=("C","D","A","A","B","B","A")
print(tup1.count("A"))

# program 4
list1=["C","D","A","A","B","B","A"]
list1.sort()
print(list1)

