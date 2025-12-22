"""Write a program that takes 'salary 'as input.Using conditional statements, calculate the final tax rate based on these rules:
• If salary < 30,000 → 5%
•If salary is 30,000 - 70,000 → 15%
•If salary > 70,000 → 25%"""

salary = int(input("Enter Your Salary: "))

if (salary < 30000):

    tax_amt = salary * 0.05
    final_salary = salary - tax_amt
    
    print(" Final Salary: ", final_salary)

elif ( salary >= 30000 and salary <= 70000):
    tax_amt = salary * 0.15
    final_salary = salary - tax_amt
    
    print(" Final Salary: ", final_salary)

elif ( salary > 70000):
    tax_amt = salary * 0.25
    final_salary = salary - tax_amt
    
    print(" Final Salary: ", final_salary) 

### Second method can be like 
# (Chatgpt did slightly helped for this )



def Calculate_FinalSalary(salary):
    if (salary < 30000):
        tax_rate =0.05
    

    elif ( salary >= 30000 and salary <= 70000):
        tax_rate = 0.15
    
    elif ( salary > 70000):
        tax_rate = 0.25

    tax_amt =  salary * tax_rate
    final_salary = salary - tax_amt
    return final_salary 


salary = int(input("Enter Your salary Here: "))
final_salary = Calculate_FinalSalary(salary)
print(final_salary )