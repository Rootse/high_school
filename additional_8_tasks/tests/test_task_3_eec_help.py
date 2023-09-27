from unittest import TestCase, main
from additional_8_tasks.task_3_eec_help import EEC_help


class TestEECHelp(TestCase):

    def test_EEC_help(self):
        self.assertTrue(EEC_help([], []))
        self.assertFalse(EEC_help([1, 2, 3], [1, 2, 3, 4]))
        self.assertTrue(EEC_help([1, 2, 3], [1, 2, 3]))
        self.assertTrue(EEC_help([1, 3, 2], [1, 2, 3]))
        self.assertFalse(EEC_help([1, 3, 2, 3], [1, 2, 2, 3]))
        self.assertTrue(EEC_help([1, 1], [1, 1]))


if __name__ == '__main__':
    main()
