from fastapi import FastAPI

app=FastAPI()

@app.get("/students")
def get_students():
    return{"this is a GET request"}

@app.post("/students")
def post_students():
    return{"this is a POST request"}

@app.put("/students")
def put_students():
    return{"this is a PUT request"}

@app.delete("/students")
def delete_students():
    return{"this is a DELETE request"}