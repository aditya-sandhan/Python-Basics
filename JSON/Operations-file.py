import json

with open("sample.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)

data = {
    "hobby":"swim",
    "date": 20
}

with open("sample.json","w") as f:
    json_str = json.dump(data, f,indent = 4)