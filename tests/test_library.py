from conftest import library, another_book, another_library


class TestLibrary:
    def test_new_library(self, library):
        assert library.name

    def test_name_in_library(self, library, another_library):
        assert library.name != another_library.name

    def test_library_name(self, library):
        assert library.name == "British"

    def test_add_book_in_library(self, library, first_book, another_book):
        library.add_book(first_book)
        library.add_book(another_book)
        assert first_book in library.books
        assert another_book in library.books
    def test_remove_book(self, library, first_book, another_book):
        library.remove_book(first_book)
        library.remove_book(another_book)
        assert first_book not in library.books
        assert another_book not in library.books