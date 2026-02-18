class BookService:
    @staticmethod
    def filter_by_min_pages(books: list, min_pages: int):
        return [b for b in books if b.pages > min_pages]