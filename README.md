# 📚 API de Biblioteca con FastAPI & GitHub Actions

Este proyecto es una **API REST** de ejemplo diseñada para gestionar una biblioteca de libros. El objetivo principal es demostrar la implementación de un pipeline de **Integración Continua (CI)** que automatiza la calidad del código, las pruebas unitarias y las pruebas de extremo a extremo (E2E).

---

## 🚀 Funcionalidad de la API

La API gestiona un recurso principal: **Libros**. Permite registrar nuevos ejemplares y realizar filtrados basados en la extensión de los mismos.

### Requisitos Técnicos:
* **Endpoint POST `/books`**: Registra un libro con título, autor, páginas y categoría.
* **Endpoint GET `/books/filter`**: Recupera libros con más de **X** páginas (parámetro de consulta).
* **Validación**: Uso de **Pydantic** para asegurar que el número de páginas sea positivo y los campos obligatorios estén presentes.
* **Lógica de Negocio**: Clase `BookService` dedicada al filtrado de datos de forma independiente a la infraestructura web.

---

## 🛠️ Estructura del Proyecto

```text
.
├── .github/workflows/  # Configuración del Pipeline (CI)
│   └── ci.yml
├── app/                # Código fuente de la aplicación
│   ├── main.py         # Rutas de FastAPI y puntos de entrada
│   ├── schemas.py      # Modelos de datos (Pydantic)
│   └── service.py      # Lógica de negocio (BookService)
├── tests/              # Suite de pruebas
│   ├── test_unit.py    # Pruebas de lógica pura (sin servidor)
│   └── test_e2e.py     # Pruebas de integración HTTP reales
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación

