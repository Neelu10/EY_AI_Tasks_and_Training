import json
import logging

logging.basicConfig(
    filename="apps.log",
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
students=[{"name":"Rahul","age":21,"course":"AI","marks":85},{"name":"Priya","age":21,"course":"AI","marks":85}]
logging.info('data added successfully')
new_student={'name':"Arjun","age":20,"course":"Data Science","marks":78}
students.append(new_student)
logging.info("new student was appended")

with open("../students.json", "r")as f:
    data=json.load(f)
logging.info("file read successfully")

with open ("../students.json", "w")as f:
    json.dump(students,f,indent=4)
logging.info("updated data saved successfully")


print(data[0]["name"])
print(data[1]["age"])