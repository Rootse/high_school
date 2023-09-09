from unittest import TestCase, main
from recursion.task_4_palindrome import is_palindrome


class TestDegree(TestCase):

    def test_is_palindrome_1(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('лёша на полке клопа нашёл'))
        self.assertTrue(is_palindrome('я арка края'))
        self.assertFalse(is_palindrome('абв'))
        self.assertFalse(is_palindrome('аббв'))
        self.assertFalse(is_palindrome('абва'))
        self.assertTrue(is_palindrome('аб ба'))


if __name__ == '__main__':
    main()
