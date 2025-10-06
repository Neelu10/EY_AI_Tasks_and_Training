from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    email: str
    is_active:bool=True

data={"name":"elsa","age":20,"email":"elsa@example.com"}
student= Student(**data)

print(student)
print(student.name)
# invalid_data={"name":"elsa","age":"twenty","email":"elsa@example.com"}
# student= Student(**invalid_data)