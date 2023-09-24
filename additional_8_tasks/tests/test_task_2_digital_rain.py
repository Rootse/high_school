from unittest import TestCase, main
from additional_8_tasks.task_2_digital_rain import digital_rain


class TestDigitalRain(TestCase):

    def test_white_walkers1(self):
        self.assertEqual(digital_rain("1111000"), "111000")
        self.assertEqual(digital_rain("11101000"), "11101000")
        self.assertEqual(digital_rain("011111110"), "10")
        self.assertEqual(digital_rain("11111111"), "")
        self.assertEqual(digital_rain("0"), "")
        self.assertEqual(digital_rain("10"), "10")


if __name__ == '__main__':
    main()
