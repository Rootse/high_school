from unittest import TestCase, main
from tasks.task_1_squirrel import squirrel, factorial


class TestFactorial(TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_seven(self):
        self.assertEqual(factorial(7), 5040)

    def test_factorial_fifty_four(self):
        self.assertEqual(factorial(54), 230843697339241380472092742683027581083278564571807941132288000000000000)

    def test_squirrel_zero(self):
        self.assertEqual(squirrel(0), 1)

    def test_squirrel_one(self):
        self.assertEqual(squirrel(1), 1)

    def test_squirrel_seven(self):
        self.assertEqual(squirrel(7), 5)

    def test_squirrel_fifty_four(self):
        self.assertEqual(squirrel(54), 2)


if __name__ == '__main__':
    main()
