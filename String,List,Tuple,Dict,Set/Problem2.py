'''Given a list of tuples with info(name,subjects) 
3)create a dictionary with name as key and subject as value'''

info = [
    ("alice","Math"),
    ("bob","Science"),
    ("alice","Science"),
    ("charlie","math"),
    ("bob","Math"),
    ("alice","English"),
    ("charlie","English")
]

dict = {}
for name, course in info:
    if(dict.get(name) == None):         # For Non Existing name
        dict.update({name: set()})
        dict[name].add(course)

    else:                               # For Existing name    
        dict[name].add(course)

print(dict)