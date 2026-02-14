data = True

with open("data.txt","r") as f:
    line = 1
    while data:
        data = f.readline()

        if ("python" in data):
            print("Python exists in file")
            print(f"its present at line {line}")
            break
        line +=1

    