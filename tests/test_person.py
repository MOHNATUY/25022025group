from conftest import another_person


class TestPerson:
    def test_new_person(self, person):
        assert person.inn
        assert person.name


class Test_inn_person:
    def test_inn_in_person(self, person, another_person):
        assert person.inn != another_person.inn
