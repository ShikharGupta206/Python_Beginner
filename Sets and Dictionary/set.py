set1={1,2,2,3,4}
print(set1)

# Set Functions
set1.add(6)
print(set1)
set1.remove(2)
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)

# Union and Intersection
set2={2,3,4,5,6}
set3={2,3,4,10,19}

print(set2.union(set3))
print(set2.intersection(set3))