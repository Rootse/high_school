from unittest import TestCase, main
from tasks.task_15_tank_rush import TankRush


class TestTankRush(TestCase):

    def test_tank_rush1(self):
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "34 98"), True)

    def test_tank_rush2(self):
        self.assertEqual(TankRush(3, 4, "1234 2334 0987", 2, 2, "34 98"), False)

    def test_tank_rush3(self):
        self.assertEqual(TankRush(3, 4, "1234 3456 9876", 2, 2, "34 98"), True)

    def test_tank_rush4(self):
        self.assertEqual(TankRush(3, 4, "1234 3498 9876", 2, 2, "34 98"), True)

    def test_tank_rush5(self):
        self.assertEqual(TankRush(3, 4, "3412 2334 0987", 2, 2, "34 98"), False)

    def test_tank_rush6(self):
        self.assertEqual(TankRush(3, 4, "3412 2335 0798", 2, 2, "34 98"), False)

    def test_tank_rush7(self):
        self.assertEqual(TankRush(4, 6, '029402 560202 029694 780288', 2, 2, '02 94'), True)

    def test_tank_rush8(self):
        self.assertEqual(TankRush(4, 6, '029402 560202 029694 780288', 2, 2, '02 88'), False)


    def test_examples(self):
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "34 87"), False)
        self.assertEqual(TankRush(3, 4, "1234 2345 0987", 2, 2, "34 98"), True)
        self.assertEqual(TankRush(3, 4, "1234 1234 1234", 3, 4, "1234 1234 1234"), True)
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 3, 1, '4 5 7'), True)
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 1, 3, '123'), True)
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 1, 2, '24'), False)

    def test_border_cases(self):
        self.assertEqual(TankRush(1, 1, "1", 1, 2, "12"), False)
        # self.assertEqual(TankRush(3, 4, '1234 2345 0987', 0, 0, ''), True)
        # self.assertEqual(TankRush(0, 0, '', 0, 0, ''), True)

    def test_equal_size(self):
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 3, 4, '1234 2345 0987'), True)
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 3, 4, '1234 1345 0987'), False)

    def test_one_symbol(self):
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 1, 1, '6'), False)
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 1, 1, '1'), True)
        self.assertEqual(TankRush(3, 4, '1234 2345 0987', 1, 1, '0'), True)

    def test_big_elem(self):
        self.assertEqual(TankRush(2, 2, '12 87', 1, 3, '121'), False)
        self.assertEqual(TankRush(2, 2, '12 87', 3, 2, '12 87 11'), False)
        self.assertEqual(TankRush(2, 2, '12 87', 3, 3, '122 872 112'), False)


if __name__ == '__main__':
    main()
