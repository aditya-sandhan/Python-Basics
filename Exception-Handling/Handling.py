try:
    num = int(input("Enter a Number: "))
    print(10/num)

except ZeroDivisionError:
    print("Division by 0 is not allowed!")

except ValueError:
    print("Invalid Input!")

else:
    print("Everything is fine and ok !")

finally:
    print("This will run even if error occurs or not")