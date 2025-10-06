class student:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

data={"name":"anna","age":18,"email":"anna@example.com"}
Student=student(**data)
print(Student.name)