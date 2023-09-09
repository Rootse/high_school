from unittest import TestCase, main
from tasks.task_16_maximum_discount import MaximumDiscount


class TestUFO(TestCase):

    def test_maximum_discount1(self):
        self.assertEqual(MaximumDiscount(7, [400, 350, 300, 250, 200, 150, 100]), 450)

    def test_maximum_discount2(self):
        self.assertEqual(MaximumDiscount(9, [300, 350, 400, 250, 200, 150, 100, 75, 50]), 500)
        self.assertEqual(MaximumDiscount(3, [300, 350, 400, ]), 300)
        self.assertEqual(MaximumDiscount(2, [300, 350,]), 0)
        self.assertEqual(MaximumDiscount(7, [300, 350, 400, 250, 100, 100, 100]), 400)
        self.assertEqual(MaximumDiscount(6, [300, 350, 400, 250, 200, 150]), 450)
        self.assertEqual(MaximumDiscount(8, [300, 350, 400, 250, 200, 150, 100, 75]), 450)
        self.assertEqual(MaximumDiscount(9, [200, 200, 200, 200, 200, 200, 200, 200, 200]), 600)

    def test_maximum_discount3(self):
        self.assertEqual(MaximumDiscount(7, [450, 300, 250, 200, 100, 150, 350]), 450)
        self.assertEqual(MaximumDiscount(5, [100, 100, 100, 100, 100]), 100)
        self.assertEqual(MaximumDiscount(3, [150, 200, 250]), 150)
        self.assertEqual(MaximumDiscount(1, [100]), 0)


if __name__ == '__main__':
    main()
