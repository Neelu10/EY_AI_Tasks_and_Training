
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()
class Employee(BaseModel):
    id:int
    name:str
    department:str
    salary:float

employees=[{"id":1,"name":"Amit Sharma","department":"Tax","salary":30000 }]

@app.get("/employees")
def get_employees():
    return{"employees":employees}

@app.post("/employees",status_code=201)
def add_employees(employee:Employee):
    employees.append(employee.model_dump())
    return{"message":"employee added successfully","employee":employee}

# @app.get("/employees/count")
# def count_employees():
#     return {"total_employees": len(employees)}

@app.get("/employees/{employee_id}")
def get_employees(employee_id:int):
    for s in employees:
        if s["id"] == employee_id:
            return s
    raise HTTPException(status_code=404, detail="employee not found")



#
@app.put("/employees/{employee_id}")
def update_employees(employee_id:int,updated_employee:Employee):
    for i,s in enumerate(employees):
        if s["id"] == employee_id:
            employees[i]=updated_employee.model_dump()
            return{"message":"employee updated successfully","employee":updated_employee}
    raise HTTPException(status_code=404, detail="employee not found")
#
@app.delete("/employees/{employee_id}")
def delete_employees(employee_id:int):
    for i,s in enumerate(employees):
        if s["id"] == employee_id:
            deleted_employee=employees.pop(i)
            return {"message": "employee deleted successfully", "employee": deleted_employee}
    raise HTTPException(status_code=404, detail="employee not found")

#
#
