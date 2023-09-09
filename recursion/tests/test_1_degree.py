from unittest import TestCase, main
from recursion.task_1_degree import degree


class TestDegree(TestCase):

    def test_degree_1(self):
        self.assertEqual(degree(5, 0), 1)
        self.assertEqual(degree(1, 1), 1)
        self.assertEqual(degree(1, 3), 1)
        self.assertEqual(degree(2, 2), 4)
        self.assertEqual(degree(2, 8), 256)
        self.assertEqual(degree(3, 3), 27)


if __name__ == '__main__':
    main()
