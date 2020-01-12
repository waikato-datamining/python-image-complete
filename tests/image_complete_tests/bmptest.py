import unittest
from .basetest import ImageCompleteTest
from image_complete.bmp import is_bmp_complete


class TestPng(ImageCompleteTest):

    def test_complete_bmp(self):
        self.assertTrue(is_bmp_complete(self.data_file("complete.bmp")))

    def test_incomplete_bmp(self):
        self.assertFalse(is_bmp_complete(self.data_file("incomplete.bmp")))

    def test_empty_bmp(self):
        self.assertFalse(is_bmp_complete(self.data_file("empty.bmp")))


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    return unittest.TestLoader().loadTestsFromTestCase(TestPng)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
