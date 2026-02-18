from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_workflow_create_and_filter():
    # 1. Crear un libro
    client.post("/books", json={"title": "Don Quijote", "author": "Cervantes", "pages": 1000, "category": "Clásico"})
    
    # 2. Filtrar libros con más de 500 páginas (Debe devolver 1)
    response = client.get("/books/filter?min_pages=500")
    assert response.status_code == 200
    assert len(response.json()) == 1
    
    # 3. Filtrar libros con más de 2000 páginas (Debe devolver 0)
    response = client.get("/books/filter?min_pages=2000")
    assert len(response.json()) == 0