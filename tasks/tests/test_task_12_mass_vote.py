from unittest import TestCase, main
from tasks.task_12_mass_vote import MassVote


class TestMassVote(TestCase):

    def test_mas_vote1(self):
        self.assertEqual(MassVote(5, [60, 10, 10, 15, 5]), "majority winner 1")

    def test_mas_vote2(self):
        self.assertEqual(MassVote(4, [111, 111, 110, 110]), "no winner")

    def test_mas_vote3(self):
        self.assertEqual(MassVote(3, [10, 15, 10]), "minority winner 2")

    def test_mas_vote4(self):
        self.assertEqual(MassVote(1, [10]), "majority winner 1")

    def test_mas_vote5(self):
        self.assertEqual(MassVote(9, [5, 10, 15, 20, 25, 35, 45, 45, 50]), "minority winner 9")


if __name__ == '__main__':
    main()
