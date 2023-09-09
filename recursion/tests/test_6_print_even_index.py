from unittest import TestCase, main
from recursion.task_6_print_even_index import print_even_index


class TestDegree(TestCase):

    def output_func(self, arr: list) -> str:
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        print_even_index(arr)

        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__

        output = output.replace('\n', '')
        return output

    def test_print_even_index(self):
        self.assertEqual(self.output_func([]), '')
        self.assertEqual(self.output_func([1]), '1')
        self.assertEqual(self.output_func([1,2,3]), '13')
        self.assertEqual(self.output_func([1, 2, 3, 4, 5]), '135')


if __name__ == '__main__':
    main()
