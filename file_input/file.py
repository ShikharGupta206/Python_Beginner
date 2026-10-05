# Replace word

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using java.\nI Like programming in java")

with open("practice.txt","r") as x:
    data=x.read()

new_data=data.replace("java","python")
print(new_data)

with open("practice.txt","w") as y:
    y.write(new_data)

# seacrh word

def check_word(word):
    with open("practice.txt","r") as x:
        data=x.read()
        
        if(data.find(word)!=-1):
            print("found")
        else:
            print("not found")

check_word("learning")

# Check line

def check_line(word):
    data=True
    line=1
    with open("practice.txt","r") as x:
        while data:
            data=x.readline()
            if(word in data):
                print(line)
                return
            line+=1
    return -1


            

check_line("lea")

# check even number

with open("number.txt","r") as f:
    data=f.read()
    print(data)
    count=0

    nums=data.split(",")
    for value in nums:
        if(int(value)%2==0):
            count+=1

    print(count)

    
            



