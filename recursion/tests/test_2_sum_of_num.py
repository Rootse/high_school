from unittest import TestCase, main
from recursion.task_2_sum_of_num import sum_of_num


class TestDegree(TestCase):

    def test_sum_of_num_1(self):
        self.assertEqual(sum_of_num(0), 0)
        self.assertEqual(sum_of_num(1), 1)
        self.assertEqual(sum_of_num(123), 6)
        self.assertEqual(sum_of_num(1024), 7)
        self.assertEqual(sum_of_num(1000), 1)
        self.assertEqual(sum_of_num(101), 2)
        self.assertEqual(sum_of_num(-150), 4)


if __name__ == '__main__':
    main()
