from unittest import TestCase, main
from tasks.task_17_line_analysis import LineAnalysis


class TestLineAnalysis(TestCase):

    def test_line_analysis1(self):
        self.assertEqual(LineAnalysis('*..*..*..*..*..*..*'), True)

    def test_line_analysis2(self):
        self.assertEqual(LineAnalysis('''*'''), True)

    def test_line_analysis3(self):
        self.assertEqual(LineAnalysis('''***'''), True)

    def test_line_analysis4(self):
        self.assertEqual(LineAnalysis('''*.......*.......*'''), True)

    def test_line_analysis5(self):
        self.assertEqual(LineAnalysis('''**'''), True)

    def test_line_analysis6(self):
        self.assertEqual(LineAnalysis('''*.*'''), True)

    def test_line_analysis_1(self):
        self.assertEqual(LineAnalysis("*..*..*..*..*..*..*"), True)
        self.assertEqual(LineAnalysis("*"), True)
        self.assertEqual(LineAnalysis("***"), True)
        self.assertEqual(LineAnalysis("*.......*.......*"), True)
        self.assertEqual(LineAnalysis("**"), True)
        self.assertEqual(LineAnalysis("*.*"), True)
        self.assertEqual(LineAnalysis("*..*...*..*..*..*..*"), False)
        self.assertEqual(LineAnalysis("*..*..*..*..*..**..*"), False)
        self.assertEqual(LineAnalysis("**..*..*..*..*..**..*"), False)
        self.assertEqual(LineAnalysis("**..*..*..*..*..**..**"), False)
        self.assertEqual(LineAnalysis("**..*"), False)
        self.assertEqual(LineAnalysis("**..***"), False)
        self.assertEqual(LineAnalysis("**.."), False)
        self.assertEqual(LineAnalysis("*..**..**"), False)

    def test_line_analysis_2(self):
        self.assertEqual(LineAnalysis('*'), True)
        self.assertEqual(LineAnalysis('***'), True)
        self.assertEqual(LineAnalysis('*.*'), True)
        self.assertEqual(LineAnalysis('**.'), False)
        self.assertEqual(LineAnalysis('.'), False)
        self.assertEqual(LineAnalysis('*.*.*.*'), True)
        self.assertEqual(LineAnalysis('*...*...*'), True)


if __name__ == '__main__':
    main()
