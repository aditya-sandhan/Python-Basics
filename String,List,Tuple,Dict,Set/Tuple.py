tup = (1,2,3,4,5)
print(tup)
print(type(tup))  # Output: <class 'tuple'>

tup2 = (1)  #treated as an integer
print(tup2)
print(type(tup2))  # Output: <class 'int'> ----Here, it's not a tuple 


# To change tuple
countries = ('India', 'USA', 'UK', 'Germany')
covlist = list(countries)  # Convert tuple to list
covlist.append('France')    # Modify the list
countries = tuple(covlist)  # Convert back to tuple
print(countries)