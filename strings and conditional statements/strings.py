str1="hello"
str2='hello'
str3='''Hello'''

#  They all have string data type

# Backslash
str4="hello , \n New world"
print(str4)

# Tab character
str5="hello \tNew World"
print(str5)

# Concatenation
print(str1+str2)

# Len function
# counts spacing also
print(len(str5))

# indexing
print(str1[0])

# Slicing
print(str1[0:])
print(str1[:3])
print(str1[1:len(str1)])
print(str1[-1:-3])

#  Fucntions
print(str1.endswith("o"))
print(str1.capitalize())
print(str1.replace('h','e'))
print(str1.find('e'))
print(str1.count('e'))