from unittest import TestCase, main
from tasks.task_7_word_search import WordSearch


class TestWordSearch(TestCase):

    def test_word_search_1(self):
        self.assertEqual(WordSearch(12,
                                    "строка разбивается на набор строк через выравнивание по заданной ширине.",
                                    "строк"
                                    ), [0, 0, 0, 1, 0, 0, 0])

    def test_word_search_2(self):
        self.assertEqual(WordSearch(7,
                                    "строка разбивается на набор строк через выравнивание по заданной ширине.",
                                    "разбивается"
                                    ), [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_word_search_3(self):
        self.assertEqual(WordSearch(3, '12345', '123'), [1, 0])


if __name__ == '__main__':
    main()
