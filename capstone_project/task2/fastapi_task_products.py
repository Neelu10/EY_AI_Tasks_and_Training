from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    ProductID: str
    ProductName: str
    Category: str
    Price: int

# Initial product list
products = [
    {
        "ProductID": "P101",
        "ProductName": "Laptop",
        "Category": "Electronics",
        "Price": 800
    },
    {
        "ProductID": "P102",
        "ProductName": "Mouse",
        "Category": "Accessories",
        "Price": 20
    },
    {
        "ProductID": "P103",
        "ProductName": "Keyboard",
        "Category": "Accessories",
        "Price": 35
    },
    {
        "ProductID": "P104",
        "ProductName": "Headphones",
        "Category": "Audio",
        "Price": 50
    }
]

@app.get("/products")
def get_products():
    return {"products": products}

@app.get("/products/count")
def get_products_count():
    return {"products_count": len(products)}

@app.get("/products/{product_id}")
def get_product(product_id: str):
    for p in products:
        if p["ProductID"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products", status_code=201)
def add_product(product: Product):
    products.append(product.dict())
    return {"message": "Product added successfully", "product": product}

@app.put("/products/{product_id}")
def update_product(product_id: str, updated_product: Product):
    for i, p in enumerate(products):
        if p["ProductID"] == product_id:
            products[i] = updated_product.dict()
            return {"message": "Product updated successfully", "product": updated_product}
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    for i, p in enumerate(products):
        if p["ProductID"] == product_id:
            deleted_product = products.pop(i)
            return {"message": "Product deleted successfully", "product": deleted_product}
    raise HTTPException(status_code=404, detail="Product not found")



# post data
'''{
  "ProductID": "P105",
  "ProductName": "Webcam",
  "Category": "Accessories",
  "Price": 45
}'''

#put data
'''{
  "ProductID": "P102",
  "ProductName": "Wireless Mouse",
  "Category": "Accessories",
  "Price": 30
}'''

