#Basic loop 
for i in range(5):
    print(i+1)

#Counting specific character in phrase
phrase = "Artificial intelligence"
count=0

for ch in phrase:
    if (ch == 'i'):
        count +=1

print("Count of i : ",count)


#Counting vowels in given String
str1 = "i want to be a successful entrepreneur"

count=0
for vwl in str1:
    if(vwl == 'a' or vwl=='e' or vwl=='i' or vwl=='o' or vwl=='u'):
        count +=1

print("Count of Vowels in string: ",count)