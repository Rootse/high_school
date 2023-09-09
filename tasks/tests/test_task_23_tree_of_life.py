from unittest import TestCase, main
from tasks.task_23_tree_of_life import TreeOfLife


class TestTreeOfLife(TestCase):

    def test_tree_of_life1(self):
        self.assertEqual(TreeOfLife(3, 4, 12, [".+..", "..+.", ".+.."]), [".+..", "..+.", ".+.."])

    def test_tree_of_life_1(self):
        self.assertEqual(TreeOfLife(3, 4, 4, [".+..", "..+.", ".+.."]), [".+..", "..+.", ".+.."])
        self.assertEqual(TreeOfLife(3, 4, 8, [".+..", "..+.", ".+.."]), [".+..", "..+.", ".+.."])
        self.assertEqual(TreeOfLife(3, 4, 7, [".+..", "..+.", ".+.."]), ["++++", "++++", "++++"])
        self.assertEqual(TreeOfLife(3, 4, 3, [".+..", "..+.", ".+.."]), ["++++", "++++", "++++"])
        self.assertEqual(TreeOfLife(3, 4, 11, [".+..", "..+.", ".+.."]), ["++++", "++++", "++++"])
        self.assertEqual(TreeOfLife(3, 4, 2, ["++++", "++++", "++++"]), ["....", "....", "...."])
        self.assertEqual(TreeOfLife(3, 4, 3, ["++++", "++++", "++++"]), ["++++", "++++", "++++"])
        self.assertEqual(TreeOfLife(3, 4, 4, ["....", "....", "...."]), ["....", "....", "...."])
        self.assertEqual(TreeOfLife(3, 4, 5, ["....", "....", "...."]), ["++++", "++++", "++++"])


if __name__ == '__main__':
    main()
