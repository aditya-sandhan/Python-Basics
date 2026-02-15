import json

j_str = '{"name": "Aditya","city": "Nashik","age": 20}'

py_obj = json.loads(j_str)
print(py_obj)
print(type(py_obj))



p_ob = {
    
    "name": "Aditya",
    "city": "Nashik",
    "age": 20,
    "IsTeacher" : None

}

json_str = json.dumps(p_ob)
print(json_str)
print(type(json_str))