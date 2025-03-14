import uuid


class Book:
    def __init__(self, name: str, author: str):
        self.name: str = name
        self.author: str = author
        self.inn: uuid.UUID = uuid.uuid4()

    def __str__(self):
        return f"<Book: {self.name}; Author: {self.author}; Inn: {self.inn}>"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []

    def add_book(self, Book):
        self.books.append(Book)

    def remove_book(self, inn):
        for book in self.books:
            self.books.remove(book)

