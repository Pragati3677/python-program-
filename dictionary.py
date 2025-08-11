student = {"name":"Pragati",
     "Father name":"Shantilal",
     "sername":"Shendage",
     "age":19,
     "address":"Malshiras",
     "course":"B.Tech",}
print(student)
print(student["name"])  

student["grade"] = "A"

student["age"] = 21
student.update({"age": 20})

student["address"] = "Pune"
student.pop("age") 

del student["course"]

print(student)
student.items()