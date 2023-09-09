from unittest import TestCase, main
from tasks.task_8_sum_of_the import SumOfThe


class TestSumOfThe(TestCase):

    def test_sum_of_the_1(self):
        self.assertEqual(SumOfThe(5, [10, -25, -45, -35, 5]), -45)

    def test_sum_of_the_2(self):
        self.assertEqual(SumOfThe(7, [-25, 90, 10, 100, 90, -35, -50]), 90)

    def test_sum_of_the_3(self):
        self.assertEqual(SumOfThe(2, [-25, -25]), -25)

    def test_sum_of_the_4(self):
        self.assertEqual(SumOfThe(3, [50, 25, -25]), 25)


if __name__ == '__main__':
    main()
