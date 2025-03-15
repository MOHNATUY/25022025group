class TestBook:
    def test_new_book(self, first_book):
        assert first_book.inn
        assert first_book.name
        assert first_book.author

    def test_inn_in_book(self, first_book, another_book):
        assert first_book.inn != another_book.inn
