import unittest
from main import BooksCollector

class TestBooksCollector(unittest.TestCase):
    def setUp(self):
        self.books_collector = BooksCollector()

    def test_add_new_book(self):
        # Проверяем успешное добавление новой книги
        self.books_collector.add_new_book("Book1")
        self.assertIn("Book1", self.books_collector.books_genre)

        # Проверяем, что книга не добавляется повторно
        self.books_collector.add_new_book("Book1")
        self.assertNotIn("Book1", self.books_collector.books_genre)

        # Проверяем, что книга не добавляется, если ее название содержит более 40 символов
        long_name = "a" * 41
        self.books_collector.add_new_book(long_name)
        self.assertNotIn(long_name, self.books_collector.books_genre)

    def test_set_book_genre(self):
        # Проверяем установку жанра книги
        self.books_collector.add_new_book("Book1")
        self.books_collector.set_book_genre("Book1", "Фантастика")
        self.assertEqual(self.books_collector.get_book_genre("Book1"), "Фантастика")

        # Проверяем, что жанр не устанавливается, если книга не присутствует в словаре
        self.books_collector.set_book_genre("UnknownBook", "Фантастика")
        self.assertIsNone(self.books_collector.get_book_genre("UnknownBook"))

        # Проверяем, что жанр не устанавливается, если указанный жанр не входит в список доступных жанров
        self.books_collector.add_new_book("Book2")
        self.books_collector.set_book_genre("Book2", "НеизвестныйЖанр")
        self.assertNotEqual(self.books_collector.get_book_genre("Book2"), "НеизвестныйЖанр")

    def test_get_book_genre(self):
        # Проверяем, что метод возвращает корректный жанр книги по ее имени
        self.books_collector.add_new_book("Book1")
        self.books_collector.set_book_genre("Book1", "Фантастика")
        self.assertEqual(self.books_collector.get_book_genre("Book1"), "Фантастика")

        # Проверяем, что метод возвращает None, если книги с таким именем нет в словаре
        self.assertIsNone(self.books_collector.get_book_genre("UnknownBook"))

    def test_get_books_with_specific_genre(self):
        # Проверяем, что метод возвращает список книг с определенным жанром
        self.books_collector.add_new_book("Book1")
        self.books_collector.set_book_genre("Book1", "Фантастика")
        self.assertEqual(self.books_collector.get_books_with_specific_genre("Фантастика"), ["Book1"])

        # Проверяем, что метод возвращает пустой список, если книг с указанным жанром нет
        self.assertEqual(self.books_collector.get_books_with_specific_genre("Документальные фильмы"), [])

    def test_get_books_for_children(self):
        # Проверяем, что метод возвращает список книг, подходящих для детей
        self.books_collector.add_new_book("Book1")
        self.books_collector.set_book_genre("Book1", "Мультфильмы")
        self.books_collector.add_new_book("Book2")
        self.books_collector.set_book_genre("Book2", "Детективы")
        self.assertEqual(self.books_collector.get_books_for_children(), ["Book1"])

    def test_add_book_in_favorites(self):
        # Проверяем, что книга успешно добавляется в список избранных
        self.books_collector.add_new_book("Book1")
        self.books_collector.add_book_in_favorites("Book1")
        self.assertIn("Book1", self.books_collector.get_list_of_favorites_books())

        # Проверяем, что книга не добавляется повторно в список избранных
        self.books_collector.add_book_in_favorites("Book1")
        self.assertEqual(len(self.books_collector.get_list_of_favorites_books()), 1)

    def test_delete_book_from_favorites(self):
        # Проверяем, что книга успешно удаляется из списка избранных, если она там есть
        self.books_collector.add_new_book("Book1")
        self.books_collector.add_book_in_favorites("Book1")
        self.books_collector.delete_book_from_favorites("Book1")
        self.assertNotIn("Book1", self.books_collector.get_list_of_favorites_books())

        # Проверяем, что метод не вызывает ошибку, если книги нет в списке избранных
        self.books_collector.delete_book_from_favorites("UnknownBook")
        self.assertEqual(len(self.books_collector.get_list_of_favorites_books()), 0)

    def test_get_list_of_favorites_books(self):
        # Проверяем, что метод возвращает список избранных книг
        self.books_collector.add_new_book("Book1")
        self.books_collector.add_book_in_favorites("Book1")
        self.books_collector.add_new_book("Book2")
        self.books_collector.add_book_in_favorites("Book2")
        self.assertEqual(self.books_collector.get_list_of_favorites_books(), ["Book1", "Book2"])

if __name__ == '__main__':
    unittest.main()
