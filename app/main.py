from fastapi import FastAPI, Query, HTTPException
from app.schemas import Book, BookCreate
from app.service import BookService

app = FastAPI(title="Biblioteca API")

books = []

@app.post("/books", response_model=Book)
def create_book(book_data: BookCreate):
    new_id = len(books) + 1
    
    new_book = Book(id=new_id, **book_data.model_dump())
    books.append(new_book)
    
    return new_book

@app.get("/books/filter", response_model=list[Book])
def get_books_by_pages(min_pages: int = Query(..., gt=0)):
    filtered = BookService.filter_by_min_pages(books, min_pages)
    
    return filtered