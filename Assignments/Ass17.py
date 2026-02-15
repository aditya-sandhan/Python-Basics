'''Create an abstract class Employee with an abstract method calculate_salary().
Create subclasses Intern, FullTimeEmployee, 
and ContractEmployee that implement the method differently'''


from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self,stipend):
        self.stipend = stipend
        
    def calculate_salary(self):
        return self.stipend

class FullTimeEmployee(Employee):
    def __init__(self,base_salary,bonus):
        self.base_salary = base_salary
        self.bonus = bonus
        
    def calculate_salary(self):
        return self.base_salary + self.bonus

class ContractEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

obj1 = Intern(3000)
print(obj1.calculate_salary())

obj2 = FullTimeEmployee(50_000,20_000)
print(obj2.calculate_salary())

obj3 = ContractEmployee(200,10)
print(obj3.calculate_salary())