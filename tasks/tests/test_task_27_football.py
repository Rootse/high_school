from unittest import TestCase, main
from tasks.task_27_football import Football


class TestFootball(TestCase):

    def test_football1(self):
        self.assertTrue(Football([1, 3, 2], 3))

    def test_football2(self):
        self.assertTrue(Football([3, 2, 1], 3))

    def test_football3(self):
        self.assertTrue(Football([1, 7, 5, 3, 9], 5))

    def test_football4(self):
        self.assertFalse(Football([9, 5, 3, 7, 1], 5))

    def test_football5(self):
        self.assertTrue(Football([1, 4, 3, 2, 5], 5))

    def test_football6(self):
        self.assertFalse(Football([3, 1, 2], 3))

    def test_football7(self):
        self.assertFalse(Football([1, 2, 3], 3))

if __name__ == '__main__':
    main()
