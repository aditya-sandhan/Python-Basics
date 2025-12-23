## Progress update – string practice

a = 5
b = 10
sum = a + b

#normal formatting
print("The sum of {} and {} is {}".format(a, b, sum))

#positional formatting
print("The sum of {0} and {1} is {2}".format(a,b,sum))
print("The sum of {1} and {0} is {2}".format(a,b,sum))

#value formatting
print("Values are {a} and {b}".format(a=10,b=20))


'''F-Strings Formatting (Python 3.6+)'''

x = 20
y = 40

print(f"The sum of {x} and {y} is {x + y}")
print(f"The Average of {x} and {y} is {(x + y)/2}")

#Used more for easier implementations for variables and expressions directly in the string.
#Literal string interpolation.