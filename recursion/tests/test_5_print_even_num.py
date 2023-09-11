from unittest import TestCase, main
from recursion.task_5_print_even_num import print_even_num


class TestDegree(TestCase):

    def output_func(self, numbers: list[int]) -> str:
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        print_even_num(numbers)

        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__

        output = output.replace('\n', '')
        return output

    def test_print_even_num(self):
        self.assertEqual(self.output_func([]), '')
        self.assertEqual(self.output_func([1]), '')
        self.assertEqual(self.output_func([2]), '2')
        self.assertEqual(self.output_func([1, 2, 3]), '2')
        self.assertEqual(self.output_func([1, 2, 3, 4]), '24')
        self.assertEqual(self.output_func([1, 2, 3, 4, 5]), '24')


if __name__ == '__main__':
    main()
