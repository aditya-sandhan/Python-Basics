class Student:
    college_name = "ABC University"     # Class Attribute - belongs to class
    def __init__(self,name,cgpa):
        self.name = name            # Instance Attribute - belongs to object  
        self.cgpa = cgpa            # Instance Attribute - Can Only be invoked by obj name  

s1 = Student("Aditya",9.2)
s2 = Student("Rahul",9.0)

print(s1.name, s1.cgpa)
print(s2.name,s2.cgpa)
print(Student.college_name, s1.college_name, s2.college_name) # Class attribute can be invoked by both class or object name

class Cal:
    PI = 3.1

    def __init__(self):
        self.PI = 3.14

C1 = Cal()
print(C1.PI)    # Preferance is given to Instance PI rather than class PI
