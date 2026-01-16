'''WAF to return the count the number of digits in a number n.'''

def count_no(n):
    count = 0
    while n>0:
        i = n%10
        n = n//10

        count +=1  # right to left approach
    
    return count 


n = int(input("Enter The Number: "))
print(count_no(n)) 



# My First try -->

def count_no(n):
    a= str(n)
    return len(a)

print(count_no(1234))
