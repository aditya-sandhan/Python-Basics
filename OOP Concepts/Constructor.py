class student:
    def __init__(self):    #Default Constructor - INIT menthod is used to initialize object
        print("Hey, This is Default Constructor")

s1 = student()          #Called automatically when an object is created!
s2 = student()


class Student:
    def __init__(self,name,age):    # Parameterized Constructor
        self.name = name
        self.age = age

S1 = Student("Aditya",12)       # Passing parameters through Objects 
S2 = Student("Raj", 14)

print(f"{S1.name} is {S1.age} old")
print(f"{S2.name} is {S2.age} old")