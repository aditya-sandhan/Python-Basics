'''Write a function that prints the digit of a number n, like n=312 then it would be 3  2  1.'''


def print_digits(n):
    while n>0:
        i = n%10        # 123%10 --> 12.3 this will store Decimal value in i (i.e., 3)
        
        print(i)        # this will print i
        n = n//10       # removes the rightmost value for now i.e 3

n= int(input("Enter the number: "))
print_digits(n)
        