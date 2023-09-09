from unittest import TestCase, main
from recursion.task_9_brackets import brackets1, brackets2


class TestDegree(TestCase):

    def test_brackets_1(self):
        self.assertEqual(brackets1(0), [''])
        self.assertEqual(brackets1(1), ['()'])
        self.assertEqual(brackets1(2), ['()()', '(())'])
        self.assertEqual(brackets1(3), ['()()()', '()(())', '(())()', '(()())', '((()))'])

    def test_brackets_2(self):
        self.assertEqual(brackets2(0), [''])
        self.assertEqual(brackets2(1), ['()'])
        self.assertEqual(brackets2(2), ['(())', '()()'])
        self.assertEqual(brackets2(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])


if __name__ == '__main__':
    main()
