'''WAF to return the sum of digits of a number n.'''

def sum_of_digit(n):
    digit_sum = 0
    while (n>0):
        i = n%10
        sum += i
        
        n= n//10

    return digit_sum

n = int(input("ENTER THE NUMBER: "))
print(sum_of_digit(n))