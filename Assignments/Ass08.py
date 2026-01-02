'''Ask the user for a string and check whether it is a palindrome or not.'''

string_ip = input("Enter a string: ")

if (string_ip == string_ip[::-1]):          #Jumps from last index till 0th Index
    print("The Given Word is a Palindrome")
else:
    print("The Given Word is NOT a Palindrome")