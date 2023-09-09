from unittest import TestCase, main
from tasks.task_26_white_walkers import white_walkers


class TestWhiteWalkers(TestCase):

    def test_white_walkers1(self):
        self.assertTrue(white_walkers("axxb6===4xaf5===eee5"))

    def test_white_walkers2(self):
        self.assertFalse(white_walkers("5==ooooooo=5=5"))

    def test_white_walkers3(self):
        self.assertTrue(white_walkers("abc=7==hdjs=3gg1=======5"))

    def test_white_walkers4(self):
        self.assertFalse(white_walkers("aaS=8"))

    def test_white_walkers5(self):
        self.assertTrue(white_walkers("9===1===9===1===9"))

    def test_white_walkers6(self):
        self.assertFalse(white_walkers("aaS==="))


if __name__ == '__main__':
    main()
