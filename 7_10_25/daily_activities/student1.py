from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"message":"welcome to fastapi demo"}

@app.get("/student/{student_id}")
def get_student(student_id):
    return {"student_id":student_id,"name":"Rahul","age":23,"course":"AI" }