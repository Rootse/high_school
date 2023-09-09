from unittest import TestCase, main
from tasks.task_18_mister_robot import MisterRobot


class TestMisterRobot(TestCase):

    def test_mister_robot1(self):
        self.assertEqual(MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]), True)

    def test_mister_robot2(self):
        self.assertEqual(MisterRobot(5, [2, 3, 1, 4, 5]), True)

    def test_mister_robot3(self):
        self.assertEqual(MisterRobot(10, [1, 10, 3, 4, 5, 6, 7, 8, 9, 2]), True)

    def test_mister_robot4(self):
        self.assertEqual(MisterRobot(10, [1, 2, 10, 4, 5, 6, 7, 8, 9, 3]), False)

    def test_mister_robot_1(self):
        self.assertEqual(MisterRobot(10, [1, 3, 4, 2, 5, 6, 7, 8, 9, 10]), True)
        self.assertEqual(MisterRobot(5, [1, 3, 4, 2, 5]), True)
        self.assertEqual(MisterRobot(5, [4, 3, 2, 1, 5]), False)
        self.assertEqual(MisterRobot(5, [1, 2, 4, 3, 5]), False)
        self.assertEqual(MisterRobot(5, [2, 3, 1, 4, 5]), True)
        self.assertEqual(MisterRobot(10, [1, 3, 4, 9, 5, 6, 7, 8, 2, 10]), False)
        self.assertEqual(MisterRobot(10, [1, 3, 4, 5, 6, 7, 8, 2, 9, 10]), True)
        self.assertEqual(MisterRobot(5, [1, 4, 2, 3, 5]), True)
        self.assertEqual(MisterRobot(7, [1, 3, 4, 2, 5, 6, 7]), True)
        self.assertEqual(MisterRobot(7, [1, 7, 4, 2, 5, 6, 3]), False)


if __name__ == '__main__':
    main()
