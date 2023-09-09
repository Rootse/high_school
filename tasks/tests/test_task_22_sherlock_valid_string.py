from unittest import TestCase, main
from tasks.task_22_sherlock_valid_string import SherlockValidString


class TestSherlockValidString(TestCase):

    def test_sherlock_valid_string1(self):
        self.assertEqual(SherlockValidString("xyz"), True)
        self.assertEqual(SherlockValidString("xyzaa"), True)
        self.assertEqual(SherlockValidString("xxyyz"), True)
        self.assertEqual(SherlockValidString("xyzzz"), False)
        self.assertEqual(SherlockValidString("xxyyza"), False)
        self.assertEqual(SherlockValidString("xxyyzabc"), False)

    def test_sherlock_valid_string_1(self):
        self.assertTrue(SherlockValidString("xyz"))
        self.assertTrue(SherlockValidString("xyzaa"))
        self.assertTrue(SherlockValidString("xxyyz"))
        self.assertTrue(SherlockValidString("xxyyzziii"))
        self.assertTrue(SherlockValidString("xyzxyzt"))
        self.assertTrue(SherlockValidString("xzzz"))
        self.assertTrue(SherlockValidString("xz"))
        self.assertTrue(SherlockValidString("xxxxxyyyyyy"))
        self.assertTrue(SherlockValidString("xyzxyzttt"))

    def test_sherlock_valid_string_2(self):
        self.assertFalse(SherlockValidString("xyzzz"))
        self.assertFalse(SherlockValidString("xxyyza"))
        self.assertFalse(SherlockValidString("xxyyzabc"))
        self.assertFalse(SherlockValidString("xxyyzzzz"))
        self.assertFalse(SherlockValidString("xxyyzzziiioo"))
        self.assertFalse(SherlockValidString("xxzzzz"))
        self.assertFalse(SherlockValidString("xxxxxyyyyyyy"))
        self.assertFalse(SherlockValidString("xyzxyztttt"))


if __name__ == '__main__':
    main()
