from unittest import TestCase, main
from recursion.task_4_palindrome import is_palindrome1, is_palindrome2, is_palindrome3


class TestDegree(TestCase):

    def test_is_palindrome_1(self):
        self.assertTrue(is_palindrome1(''))
        self.assertTrue(is_palindrome1('a'))
        self.assertTrue(is_palindrome1('лёша на полке клопа нашёл'))
        self.assertTrue(is_palindrome1('я арка края'))
        self.assertFalse(is_palindrome1('абв'))
        self.assertFalse(is_palindrome1('аббв'))
        self.assertFalse(is_palindrome1('абва'))
        self.assertTrue(is_palindrome1('аб ба'))

    def test_is_palindrome_2(self):
        self.assertTrue(is_palindrome2(''))
        self.assertTrue(is_palindrome2('a'))
        self.assertTrue(is_palindrome2('лёша на полке клопа нашёл'))
        self.assertTrue(is_palindrome2('я арка края'))
        self.assertFalse(is_palindrome2('абв'))
        self.assertFalse(is_palindrome2('аббв'))
        self.assertFalse(is_palindrome2('абва'))
        self.assertTrue(is_palindrome2('аб ба'))

    def test_is_palindrome_3(self):
        self.assertTrue(is_palindrome3(''))
        self.assertTrue(is_palindrome3('a'))
        self.assertTrue(is_palindrome3('лёша на полке клопа нашёл'))
        self.assertTrue(is_palindrome3('я арка края'))
        self.assertFalse(is_palindrome3('абв'))
        self.assertFalse(is_palindrome3('аббв'))
        self.assertFalse(is_palindrome3('абва'))
        self.assertTrue(is_palindrome3('аб ба'))

if __name__ == '__main__':
    main()
