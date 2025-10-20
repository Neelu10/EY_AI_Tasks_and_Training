
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Customer(BaseModel):
    CustomerID: str
    Name: str
    Email: str
    Country: str


customers = [
    {
        "CustomerID": "C001",
        "Name": "Neha",
        "Email": "neha@example.com",
        "Country": "India"
    },
    {
        "CustomerID": "C002",
        "Name": "Ali",
        "Email": "ali@example.com",
        "Country": "UAE"
    },
    {
        "CustomerID": "C003",
        "Name": "Sophia",
        "Email": "sophia@example.com",
        "Country": "UK"
    }
]

@app.get("/customers")
def get_customers():
    return {"customers": customers}

@app.get("/customers/count")
def get_customers_count():
    return {"customers_count": len(customers)}

@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):
    for c in customers:
        if c["CustomerID"] == customer_id:
            return c
    raise HTTPException(status_code=404, detail="Customer not found")

@app.post("/customers", status_code=201)
def add_customer(customer: Customer):
    customers.append(customer.dict())
    return {"message": "Customer added successfully", "customer": customer}

@app.put("/customers/{customer_id}")
def update_customer(customer_id: str, updated_customer: Customer):
    for i, c in enumerate(customers):
        if c["CustomerID"] == customer_id:
            customers[i] = updated_customer.dict()
            return {"message": "Customer updated successfully", "customer": updated_customer}
    raise HTTPException(status_code=404, detail="Customer not found")

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: str):
    for i, c in enumerate(customers):
        if c["CustomerID"] == customer_id:
            deleted_customer = customers.pop(i)
            return {"message": "Customer deleted successfully", "customer": deleted_customer}
    raise HTTPException(status_code=404, detail="Customer not found")

#Post data

'''{
  "CustomerID": "C004",
  "Name": "John",
  "Email": "john@example.com",
  "Country": "USA"
}'''

#put data
'''{
  "CustomerID": "C002",
  "Name": "Ali Khan",
  "Email": "alikhan@example.com",
  "Country": "UAE"
}'''