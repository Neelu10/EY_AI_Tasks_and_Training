student= {
"name" :"Neelu",
"age" : 22,
"course" : "AI&DS"

}

print(student["name"]) #access by key
print(student.get("age"))

student["grade"]="A"
student["age"]= 23

student.pop("course")
del student["grade"]
print(student)

for key,value in student.items():
    print(key,":",value)