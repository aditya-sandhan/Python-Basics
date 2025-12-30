# Dictionary in Python - Mutable and Unordered collection of key-value pairs

dict1 = {
    "name" : "Aditya Sandhan",
    "Marks" : [10,15,12],
    "Age": 20           
}

print(dict1)  
print(type(dict1))      

dict1["Age"] = 24   # Updating Age
dict1["City"] = "Pune"  # Adding new key-value pair
print(dict1)