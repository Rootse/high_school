from unittest import TestCase, main
from tasks.task_21_bigger_greater import BiggerGreater


class TestBiggerGreater(TestCase):

    def test_bigger_greater1(self):
        self.assertEqual(BiggerGreater("ая"), "яа")
        self.assertEqual(BiggerGreater('fff'), '')
        self.assertEqual(BiggerGreater("нклм"), "нкмл")
        self.assertEqual(BiggerGreater("вибк"), "викб")
        self.assertEqual(BiggerGreater("вкиб"), "ибвк")

    def test_bigger_greater2(self):
        self.assertEqual(BiggerGreater('za'), '')
        self.assertEqual(BiggerGreater("а"), "")
        self.assertEqual(BiggerGreater(""), "")


if __name__ == '__main__':
    main()
