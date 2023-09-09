from unittest import TestCase, main
from tasks.task_4_mad_max import MadMax


class TestMadMax(TestCase):

    def test_mad_max_1(self):
        self.assertEqual(MadMax(1, [1]), [1])

    def test_mad_max_2(self):
        self.assertEqual(MadMax(3, [1, 2, 3]), [1, 3, 2])

    def test_mad_max_3(self):
        self.assertEqual(MadMax(7, [1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 7, 6, 5, 4])




if __name__ == '__main__':
    main()
