def Hello():
    print("hey buddy!")

Hello()


# Average of 3 numbers 

def avgval(a,b,c):
    avg = (a+b+c)/3
    return avg

a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))

print(avgval(a,b,c))


#Lambda funtions 

avg= lambda a,b,c : (a+b+c)/3    #used only for easy or single line expressions 
print(avg(3,4,5))

sum = lambda a,b: a+b
print(sum(4,5))