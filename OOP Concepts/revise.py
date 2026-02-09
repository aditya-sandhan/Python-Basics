class Student:
    subject = "Python"
    
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
        print(f"{self.name} has a cgpa of {self.cgpa}")  # for all object 
        
s1 = Student("Aditya",9.2)
s2 = Student("Raj",8.95)

# print(f"{s1.name} has a cgpa of {s1.cgpa}")    ----- for particular obj

'''--------------------------------------------------------------------------'''

class Animal:
    habitat = "South Africa"        #Class Attribute - invoked using class aswellas Object name 

    def __init__(self, name, sound):
        self.name  = name           #Instance Attribute - invoked using only Obj name 
        self.sound = sound 

A1 = Animal("Lion","Roar")
A2 = Animal("Hippo","baaa")

print(f"{A1.name} has a sound as {A1.sound} and lives in {A1.habitat}")
print(f"{A2.name} has a sound as {A2.sound} and lives in {A2.habitat}")
    