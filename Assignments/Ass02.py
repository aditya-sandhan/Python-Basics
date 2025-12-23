""" Write a function that takes two integers a and b and prints all even numbers between them (inclusive)"""


def find_even_no(a,b):
    for i in range(a,b+1):
        if(i%2 == 0):
            print(f"{i} is even number in range of {a} & {b}")


a= int(input("Enter Value of a: "))
b= int(input("Enter Value of b: "))
find_even_no(a,b)