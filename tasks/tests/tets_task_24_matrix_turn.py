from unittest import TestCase, main
from tasks.task_24_matrix_turn import MatrixTurn


class TestMatrixTurn(TestCase):

    def test_matrix_turn1(self):
        matrix = ["123456", "234567", "345678", "456789"]
        MatrixTurn(matrix, 4, 6, 3)
        self.assertEqual(matrix, ['432123', '565434', '676545', '789876'])

    def test_matrix_turn2(self):
        matrix = ["1234", "5678"]
        MatrixTurn(matrix, 2, 4, 3)
        self.assertEqual(matrix, ['7651', '8432'])

    def test_matrix_turn_1(self):
        matrix = ["123456", "234567", "345678", "456789"]
        MatrixTurn(matrix, 4, 6, 1)
        self.assertEqual(matrix,['212345', '343456', '456767', '567898'])

        matrix = ["12", "34"]
        MatrixTurn(matrix, 2, 2, 1)
        self.assertEqual(matrix, ['31', '42'])

        matrix = ["12", "34"]
        MatrixTurn(matrix, 2, 2, 4)
        self.assertEqual(matrix, ["12", "34"])

        matrix = ["123456", "234567", "345678", "456789"]
        MatrixTurn(matrix, 4, 6, 16)
        self.assertEqual(matrix, ["123456", "234567", "345678", "456789"])

        matrix = ["000000", "111111", "000000", "111111", "000000", "111111"]
        MatrixTurn(matrix, 6, 6, 1)
        self.assertEqual(matrix, ["100000", "001110", "111011", "001000", "100011", "111110"])


if __name__ == '__main__':
    main()
