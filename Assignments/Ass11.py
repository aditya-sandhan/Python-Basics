'''Create a class Student with private name, roll_number, and marks.
 Provide getter and setter methods with validation,
 e.g., marks/roll number has to be between 1 & 100 & name cannot be empty'''


class Student:
    def __init__(self,name,roll_no,marks):
        self.set_name(name) 
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    def set_name(self,name):
        if name.strip() != "" :
            self.__name = name
        else:
            print("Name can't be empty")
        
    def get_name(self):
        return self.__name
    
    def set_roll_no(self, roll_no):
        if (1 <= roll_no <= 100):
            self.__roll_no = roll_no
        else:
            print("Invalid roll number")

    def get_roll_no(self):
        return self.__roll_no
    
    def set_marks(self, marks):
        if (1 <= marks <= 100):
            self.__marks = marks
        else:
            print("Invalid marks entered ")

    def get_marks(self):
        return self.__marks
        

s = Student("Aditya",69,100)
print(s.get_name())
print(s.get_marks())
print(s.get_roll_no())

