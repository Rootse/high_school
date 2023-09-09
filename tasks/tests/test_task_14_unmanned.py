from unittest import TestCase, main
from tasks.task_14_unmanned import Unmanned


class TestUnmanned(TestCase):

    def test_unmanned1(self):
        self.assertEqual(Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]]), 12)

    def test_unmanned2(self):
        self.assertEqual(Unmanned(10, 0, [[]]), 10)

    def test_unmanned3(self):
        self.assertEqual(Unmanned(10, 2, [[3, 8, 5], [5, 2, 2]]), 15)

    def test_unmanned4(self):
        self.assertEqual(Unmanned(10, 2, [[3, 8, 5], [5, 3, 2]]), 18)

    def test_unmanned5(self):
        self.assertEqual(Unmanned(10, 2, [[11, 5, 5], [15, 2, 2]]), 10)

    def test_unmanned6(self):
        self.assertEqual(Unmanned(10, 3, [[5, 5, 3], [15, 2, 2], [20, 6, 3]]), 10)

    def test_unmanned7(self):
        self.assertEqual(Unmanned(10, 1, [[6, 5, 5]]), 10)

    def test_unmanned8(self):
        self.assertEqual(Unmanned(5, 1, [[1, 5, 5]]), 9)

    def test_unmanned9(self):
        self.assertEqual(Unmanned(154, 1, [[145, 2, 2]]), 155)

    def test_unmanned10(self):
        self.assertEqual(Unmanned(
            20, 3, [[7, 4, 2], [9, 2, 4], [13, 5, 4]]), 30
        )

    def test_unmanned11(self):
        self.assertEqual(Unmanned(10, 2, [[11, 5, 5], [15, 2, 2]]), 10)

    def test_unmanned12(self):
        self.assertEqual(Unmanned(10, 2, [[4, 5, 5], [15, 2, 2]]), 10)


if __name__ == '__main__':
    main()
