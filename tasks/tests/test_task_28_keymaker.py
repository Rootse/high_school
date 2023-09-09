from unittest import TestCase, main
from tasks.task_28_keymaker import Keymaker


class TestKeymaker(TestCase):

    def test_keymaker1(self):
        self.assertEqual(Keymaker(1), "1")
        self.assertEqual(Keymaker(2), "10")
        self.assertEqual(Keymaker(3), "100")
        self.assertEqual(Keymaker(4), "1001")
        self.assertEqual(Keymaker(5), "10010")
        self.assertEqual(Keymaker(6), "100100")
        self.assertEqual(Keymaker(7), "1001000")
        self.assertEqual(Keymaker(8), "10010000")
        self.assertEqual(Keymaker(9), "100100001")
        self.assertEqual(Keymaker(10), "1001000010")
        self.assertEqual(Keymaker(16), "1001000010000001")
        self.assertEqual(Keymaker(100), "1001000010000001000000001000000000010000000000001000000000000001000000000000000010000000000000000001")


if __name__ == '__main__':
    main()
