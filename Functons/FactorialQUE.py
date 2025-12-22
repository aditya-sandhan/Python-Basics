
# Program to calculate Factorial of N number 

def calc_fact(n):
    fact =1
    for i in range(1,n+1):
        fact =fact*i            # gets multiplied as i changes after every iteration !
                                # THODA CONFUSING THA BUT THIK AA YR
    print("Factorial of the Given number is : ",fact)


n= int(input("Enter the number: "))
calc_fact(n)