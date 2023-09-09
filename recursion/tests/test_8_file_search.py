from unittest import TestCase, main
from recursion.task_8_file_search import file_search
import os
from shutil import rmtree


class TestDegree(TestCase):
    def setUp(self):
        self.test_dir = "test_dir"
        os.mkdir(self.test_dir)

        open(f"{self.test_dir}/file1.txt", "w").close()
        os.mkdir(f"{self.test_dir}/dir1")
        open(f"{self.test_dir}/dir1/file2.txt", "w").close()
        os.mkdir(f"{self.test_dir}/dir1/dir2")
        open(f"{self.test_dir}/dir1/dir2/file3.txt", "w").close()

    def tearDown(self):
        rmtree(self.test_dir)

    def test_file_search_1(self):
        path = "./test_dir"
        depth = 1
        expected_files = ["./test_dir/file1.txt"]
        self.assertEqual(file_search(path, depth), expected_files)

    def test_file_search_2(self):
        path = "./test_dir"
        depth = 2
        expected_files = ["./test_dir/file1.txt", "./test_dir/dir1/file2.txt"]
        self.assertEqual(file_search(path, depth), expected_files)

    def test_file_search_3(self):
        path = "./test_dir"
        depth = 3
        expected_files = ["./test_dir/file1.txt", "./test_dir/dir1/file2.txt", "./test_dir/dir1/dir2/file3.txt"]
        self.assertEqual(file_search(path, depth), expected_files)


if __name__ == '__main__':
    main()
