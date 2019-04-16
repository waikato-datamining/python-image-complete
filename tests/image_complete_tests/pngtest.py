import unittest
from .basetest import ImageCompleteTest
from image_complete.png import is_png_complete


class TestPng(ImageCompleteTest):

    def test_complete_png(self):
        self.assertTrue(is_png_complete(self.data_file("complete.png")))

    def test_incomplete_png(self):
        self.assertFalse(is_png_complete(self.data_file("incomplete.png")))

    def test_empty_png(self):
        self.assertFalse(is_png_complete(self.data_file("empty.png")))


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    return unittest.TestLoader().loadTestsFromTestCase(TestPng)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
