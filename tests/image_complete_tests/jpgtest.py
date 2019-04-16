import unittest
from .basetest import ImageCompleteTest
from image_complete.jpg import is_jpg_complete


class TestJpg(ImageCompleteTest):

    def test_complete_jpg(self):
        self.assertTrue(is_jpg_complete(self.data_file("complete.jpg")))

    def test_incomplete_jpg(self):
        self.assertFalse(is_jpg_complete(self.data_file("incomplete.jpg")))

    def test_empty_jpg(self):
        self.assertFalse(is_jpg_complete(self.data_file("empty.jpg")))


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    return unittest.TestLoader().loadTestsFromTestCase(TestJpg)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
