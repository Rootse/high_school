from unittest import TestCase, main
from tasks.task_6_pattern_unlock import PatternUnlock


class TestPatternUnlock(TestCase):

    def test_pattern_unlock_1(self):
        self.assertEqual(PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]), "982843")

    def test_pattern_unlock_2(self):
        self.assertEqual(PatternUnlock(3, [9, 8, 7]), "2")

    def test_pattern_unlock_3(self):
        self.assertEqual(PatternUnlock(3, [1, 8, 3]), "282843")

    def test_pattern_unlock_4(self):
        self.assertEqual(PatternUnlock(10, [1, 6, 5, 4, 3, 2, 8, 9, 8, 7]), "9")


if __name__ == '__main__':
    main()