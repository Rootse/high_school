from unittest import TestCase, main
from tasks.tasks_2_odometer import odometer


class TestOdometer(TestCase):

    def test_odometer_1(self):
        self.assertEqual(odometer([]), 0)

    def test_odometer_2(self):
        self.assertEqual(odometer([10, 1, 20, 2]), 30)

    def test_odometer_3(self):
        self.assertEqual(odometer([10, 1, 20, 2, 30, 4]), 90)

    def test_odometer_4(self):
        self.assertEqual(odometer([10, 1, 15, 4, 5, 8]), 75)

    def test_odometer_5(self):
        self.assertEqual(odometer([25, 2]), 50)

    def test_odometer_6(self):
        self.assertEqual(odometer([20, 2, 30, 6, 10, 7]), 170)


if __name__ == '__main__':
    main()
