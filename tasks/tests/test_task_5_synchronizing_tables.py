from unittest import TestCase, main
from tasks.task_5_synchronizing_tables import SynchronizingTables


class TestSynchronizingTables(TestCase):

    def test_synchronizing_tables_1(self):
        self.assertEqual(SynchronizingTables(1, [1], [100000]), [100000])

    def test_synchronizing_tables_2(self):
        self.assertEqual(SynchronizingTables(3, [50, 1, 1024], [20000, 100000, 90000]), [90000, 20000, 100000])

    def test_synchronizing_tables_3(self):
        self.assertEqual(SynchronizingTables(6, [50, 1, 1024, 80, 512, 493],
                                                [20000, 100000, 90000, 95000, 30000, 50000]),
                                            [30000, 20000, 100000, 50000, 95000, 90000])


if __name__ == '__main__':
    main()
