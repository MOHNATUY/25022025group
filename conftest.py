import pytest

from models import Book, Library

@pytest.fixture(scope="session")
def first_book() -> Book:
    first_book = Book("Harry Potter", "J.K. Rowling")
    return first_book

@pytest.fixture(scope="session")
def another_book() -> Book:
    another_book = Book("The Great Gatsby", "F.Scott Fitzgerald")
    return another_book

@pytest.fixture(scope="session")
def library() -> Library:
    library = Library("British")
    return library

@pytest.fixture(scope="session")
def another_library() -> Library:
    another_library = Library("Washington")
    return another_library

