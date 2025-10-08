from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Bookstore(BaseModel):
    id: int
    title: str
    author: str
    price: float
    in_stock: bool

bookstores = [
    {"id": 1, "title": "It Starts With Us", "author": "Colleen Hoover", "price": 350.45, "in_stock": True},
    {"id": 2, "title": "Harry Potter and the Prisoner of Azkaban", "author": "J.K. Rowling", "price": 400.00, "in_stock": False},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 380.00, "in_stock": True}
]

@app.get("/bookstores")
def get_books():
    return {"bookstores":bookstores}




@app.get("/bookstores/count")
def count_books():
    return {"total_bookstores": len(bookstores)}

@app.get("/bookstores/available")
def get_available_books():
    available_books = [book for book in bookstores if book["in_stock"]]
    return {"available_books": available_books}


@app.get("/bookstores/search")
def search_books(author: Optional[str] = Query(None), max_price: Optional[float] = Query(None)):
    results = bookstores

    if author:
        results = [book for book in results if book["author"].lower() == author.lower()]

    if max_price is not None:
        results = [book for book in results if book["price"] <= max_price]

    return {"results": results}

@app.delete("/bookstores/{bookstore_id}")
def delete_bookstores(bookstore_id:int):
    for i,s in enumerate(bookstores):
        if s["id"] == bookstore_id:
            bookstores.pop(i)
            return {"message": "book details deleted successfully", "bookstores":bookstores}
    raise HTTPException(status_code=404, detail="book not found")





@app.get("/bookstores/{bookstores_id}")
def get_books(bookstores_id:int):
    for s in bookstores:
        if s["id"] == bookstores_id:
            return s
    raise HTTPException(status_code=404, detail="book not found")


@app.post("/bookstores/{bookstores_id}", status_code=201)
def add_books(bookstores_id:int,bookstore: Bookstore):
    for s in bookstores:
        if s["id"] == bookstore.id:
            raise HTTPException(status_code=400, detail="Book already exists")
    bookstores.append(bookstore.dict())
    return {"message": "Bookstore added successfully", "bookstores": bookstores_id}


@app.put("/bookstores/{bookstores_id}")
def update_bookstores(bookstores_id:int,updated_book:Bookstore):
    for i,s in enumerate(bookstores):
        if s["id"] == bookstores_id:
            bookstores[i]=updated_book.dict()
            return{"message":"book details updated successfully","bookstores":updated_book}
    raise HTTPException(status_code=404, detail="book not found")



