'''Given a list of tuples with info(name,subjects) 
1)list all unique courses 
2)list student enrolled in English'''

info = [
    ("alice","Math"),
    ("bob","Science"),
    ("alice","Science"),
    ("charlie","math"),
    ("bob","Math"),
    ("alice","English"),
    ("charlie","English")
]
course_sets = set()
for tup in info:
    course_sets.add(tup[1])

print(course_sets)

for name,course in info:
    if course == "Math":
        print(name)