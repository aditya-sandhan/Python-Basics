''' Input two list from the user. Merge them into one result and Sort them'''

list1 =[]

for i in range(1,4) :
    q = int(input(f"Enter digits {i}: "))
    list1.append(q)
    
print(list1)
list2 =[]

for i in range(4,7) :
    r = int(input(f"Enter digits {i}: "))
    list2.append(r)
    
print(list2)
list3=list1+list2
list3.sort()
print(list3)