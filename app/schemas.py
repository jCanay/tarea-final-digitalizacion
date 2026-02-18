from pydantic import BaseModel, Field

class Book(BaseModel):
    id: int
    title: str
    author: str
    pages: int
    category: str

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    pages: int = Field(..., gt=0)
    category: str