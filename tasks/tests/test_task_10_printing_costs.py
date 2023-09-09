from unittest import TestCase, main
from tasks.task_10_printing_costs import PrintingCosts


class TestPrintingCosts(TestCase):

    def test_printing_costs1(self):
        self.assertEqual(PrintingCosts("FGHJ"), 88)

    def test_printing_costs2(self):
        self.assertEqual(PrintingCosts("ПРОМв"), 5 * 23)

    def test_printing_costs3(self):
        self.assertEqual(PrintingCosts("№;%:"), 64)


if __name__ == '__main__':
    main()
