"""скрипт для тестирования методов класса"""
import pytest
from main import BooksCollector

@pytest.fixture
def books_collector():
    return BooksCollector()


def test_add_new_book(books_collector):
    """_summary_

    Args:
        books_collector (_type_): _description_
    """
    books_collector.add_new_book("Книга_1")
    assert books_collector.get_books_genre() == {"Книга_1": ""}


def test_add_new_book_with_long_name(books_collector):
    """_summary_

    Args:
        books_collector (_type_): _description_
    """
    books_collector.add_new_book("Книга имя которой определенно больше 40 символов")
    assert books_collector.get_books_genre() == {}


@pytest.mark.parametrize("name, genre, expected_genre", [
    ("Книга_1", "Фантастика", "Фантастика"),
    ("Книга_2", "Мультфильмы", "Мультфильмы"),
    ("Книга_3", "Комедии", "Комедии")
])


def test_set_book_genre_name(books_collector, name, genre, expected_genre):
    """_summary_
    Args:
        books_collector (class): _description_
        name (str): _description_
        genre (str): _description_
        expected_genre (str): _description_
    """
    books_collector.add_new_book(name)
    books_collector.set_book_genre(name, genre)
    assert books_collector.get_book_genre(name) == expected_genre


@pytest.mark.parametrize("name, expected_genre", [
    ("Книга_1", ""),
    ("Книга_2", ""),
    ("Книга_3", "")
])


def test_get_book_genre_name(books_collector, name, expected_genre):
    """_summary_
    Args:
        books_collector (class): _description_
        name (str): _description_
        genre (str): _description_
        expected_genre (str): _description_
    """
    books_collector.add_new_book(name)
    assert books_collector.get_book_genre(name) == expected_genre


@pytest.mark.parametrize("genre, expected_books", [
    ("Фантастика", ["Книга_1", "Книга_4"]),
    ("Ужасы", ["Книга_2"]),
    ("Детективы", ["Книга_3"])
])
def test_get_books_with_specific_genre_param(books_collector, genre, expected_books):
    """_summary_

    Args:
        books_collector (_type_): _description_
        genre (_type_): _description_
        expected_books (_type_): _description_
    """
    books_collector.add_new_book("Книга_1")
    books_collector.add_new_book("Книга_2")
    books_collector.add_new_book("Книга_3")
    books_collector.add_new_book("Книга_4")
    books_collector.set_book_genre("Книга_1", "Фантастика")
    books_collector.set_book_genre("Книга_2", "Ужасы")
    books_collector.set_book_genre("Книга_3", "Детективы")
    books_collector.set_book_genre("Книга_4", "Фантастика")
    books_with_specific_genre = books_collector.get_books_with_specific_genre(genre)
    assert books_with_specific_genre == expected_books


def test_get_books_genre(books_collector):
    """_summary_

    Args:
        books_collector (_type_): _description_
    """
    books_collector.add_new_book("Книга_1")
    books_collector.set_book_genre("Книга_1", "Комедии")
    assert books_collector.books_genre == {"Книга_1": "Комедии"}


def test_get_books_for_children(books_collector):
    """_summary_

    Args:
        books_collector (_type_): _description_
    """
    books_collector.add_new_book("Книга_1")
    books_collector.add_new_book("Книга_2")
    books_collector.set_book_genre("Книга_1", "Фантастика")
    books_collector.set_book_genre("Книга_2", "Ужасы")
    books_for_children = books_collector.get_books_for_children()
    assert books_for_children == ["Книга_1"]


def test_add_book_in_favorites(books_collector):
    """_summary_

    Args:
        books_collector (_type_): _description_
    """
    books_collector.add_new_book("Книга_1")
    books_collector.add_book_in_favorites("Книга_1")
    assert books_collector.get_list_of_favorites_books() == ["Книга_1"]


def test_delete_book_from_favorites(books_collector):
    """_summary_

    Args:
        books_collector (_type_): _description_
    """
    books_collector.add_new_book("Книга_1")
    books_collector.add_book_in_favorites("Книга_1")
    books_collector.delete_book_from_favorites("Книга_1")
    assert books_collector.get_list_of_favorites_books() == []


@pytest.mark.parametrize("name, expected_favourite_books", [
    ("Книга_1", ["Книга_1"]),
    ("Книга_2", ["Книга_2"])
])
def test_get_list_of_favorites_books(books_collector, name, expected_favourite_books):
    """_summary_

    Args:
        books_collector (_type_): _description_
        name (_type_): _description_
        expected_favourite_books (_type_): _description_
    """
    books_collector.add_new_book(name)
    books_collector.add_book_in_favorites(name)
    assert books_collector.get_list_of_favorites_books() == expected_favourite_books
