num = int(input("Enter the Number to be Checked : "))

if (num < 0):
    print("The Given Number is negative")

elif (num>0):
    if(num%2 == 0):
        print(f"{num} is Even Number")
    else:
        print(f"{num} is Odd Number")

else:
    print("The Number is zero")