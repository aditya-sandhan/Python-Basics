# Applying Multiple Elif's 

age = int(input("Enter your Age: "))


if (age > 0 and age <= 12):
    print("You're a CHILD")

elif (age >= 13 and age <= 19):
    print("You're a TEENAGER")

elif (age > 19 and age <= 50):
    print("You're an ADULT")

elif (age == 0):
    print("You aren't Born Yet!!!")
else:
    print("You're OLDER")
