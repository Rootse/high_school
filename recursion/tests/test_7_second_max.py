from unittest import TestCase, main
from recursion.task_7_second_max import second_max


class TestDegree(TestCase):

    def test_second_max(self):
        self.assertEqual(second_max([1]), 1)
        self.assertEqual(second_max([1, 2]), 1)
        self.assertEqual(second_max([2, 2]), 2)
        self.assertEqual(second_max([1, 2, 3]), 2)
        self.assertEqual(second_max([1, 5, 4, 3, 2, 5]), 5)


if __name__ == '__main__':
    main()
