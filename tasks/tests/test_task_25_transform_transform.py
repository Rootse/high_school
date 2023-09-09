from unittest import TestCase, main
from tasks.task_25_transform_transform import TransformTransform


class TestTransformTransform(TestCase):

    def test_transform_transform1(self):
        self.assertTrue(TransformTransform([2, 6], 2))

    def test_transform_transform2(self):
        self.assertTrue(TransformTransform([2, 6, 3, 5, 8, 7, 2, 1, 3, 4], 10))

    def test_transform_transform3(self):
        self.assertFalse(TransformTransform([1], 1))


if __name__ == '__main__':
    main()
