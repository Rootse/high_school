from unittest import TestCase, main
from tasks.task_11_big_minus import BigMinus


class TestBigMinus(TestCase):

    def test_big_minus1(self):
        self.assertEqual(BigMinus("1234567891", "1"), "1234567890")

    def test_big_minus2(self):
        self.assertEqual(BigMinus("1", "321"), "320")

    def test_big_minus3(self):
        self.assertEqual(BigMinus("7438979134693413", "432321321"), "7438978702372092")

    def test_big_minus4(self):
        self.assertEqual(BigMinus("432321321", "7438979134693413"), "7438978702372092")

    def test_big_minus5(self):
        self.assertEqual(BigMinus("1234567890", "1234567890"), "0")


if __name__ == '__main__':
    main()
