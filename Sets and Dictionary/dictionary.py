dict1={"name":"rahul","age":20,"Subject":"Maths"}
dict2={
    "name":"rahul",
    "age":20,
    "subject":["Maths","Science","History"],
    "marks":{
        "Maths":20,
        "Science":30,
        "History":50
    }
}

# Appending a value to the dictionary
print(dict2["marks"]["Maths"])
dict1["roll"]=20
print(dict1)

# Dictionary Functions
print(dict2.keys())
print(dict2.values())
print(dict2.items())
print(dict2.get("marks"))
dict2.update(dict1)
print(dict2)
