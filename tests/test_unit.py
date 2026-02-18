from app.service import BookService
from app.schemas import Book

def test_filter_by_min_pages_logic():
    books = [
        Book(id=1, title="Pequeño", author="A", pages=50, category="X"),
        Book(id=2, title="Grande", author="B", pages=500, category="Y")
    ]
    
    # Si filtramos por más de 100 páginas, solo debe quedar el libro id 2
    result = BookService.filter_by_min_pages(books, 100)
    assert len(result) == 1
    assert result[0].id == 2