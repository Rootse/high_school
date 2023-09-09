from unittest import TestCase, main
from tasks.task_13_ufo import UFO


class TestUFO(TestCase):

    def test_ufo1(self):
        self.assertEqual(UFO(2, [1234, 1777], False), [4660, 6007])

    # def test_ufo2(self):
    #     self.assertEqual(UFO(2, [9, 8], True), [4660, 6007])


if __name__ == '__main__':
    main()
