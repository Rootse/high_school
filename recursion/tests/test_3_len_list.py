from unittest import TestCase, main
from recursion.task_3_len_list import len_list


class TestDegree(TestCase):

    def test_len_list_1(self):
        self.assertEqual(len_list([]), 0)
        self.assertEqual(len_list(['']), 1)
        self.assertEqual(len_list([123]), 1)
        self.assertEqual(len_list(['1', '2', '3']), 3)
        self.assertEqual(len_list([1, 2, 3, 4, 5]), 5)


if __name__ == '__main__':
    main()
