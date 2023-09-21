from unittest import TestCase, main
from additional_8_tasks.task_1_white_walkers import white_walkers


class TestWhiteWalkers(TestCase):

    def test_white_walkers1(self):
        self.assertFalse(white_walkers(""))
        self.assertFalse(white_walkers("5p5"))
        self.assertFalse(white_walkers("==="))
        self.assertTrue(white_walkers("axxb6===4xaf5===eee5"))
        self.assertFalse(white_walkers("5==ooooooo=5=5"))
        self.assertTrue(white_walkers("abc=7==hdjs=3gg1=======5"))
        self.assertFalse(white_walkers("aaS=8"))
        self.assertTrue(white_walkers("9===1===9===1===9"))
        self.assertFalse(white_walkers("aaS==="))



if __name__ == '__main__':
    main()
