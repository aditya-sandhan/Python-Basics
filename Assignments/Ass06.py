'''WAP to print all number form 1 to 100 which are divisible by 3 and 5 both
 Hence table of 15'''


for i in range(1,101):
    if ((i%3 == 0) and (i%5 == 0)):
        print(f"{i} is divisible by both 3 and 5")

    