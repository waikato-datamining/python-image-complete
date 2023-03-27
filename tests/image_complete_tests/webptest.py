import unittest
from .basetest import ImageCompleteTest
from image_complete.webp import is_webp_complete


class TestPng(ImageCompleteTest):

    def test_complete_webp(self):
        self.assertTrue(is_webp_complete(self.data_file("complete.webp")))

    def test_incomplete_webp(self):
        self.assertFalse(is_webp_complete(self.data_file("incomplete.webp")))

    def test_empty_webp(self):
        self.assertFalse(is_webp_complete(self.data_file("empty.webp")))


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    return unittest.TestLoader().loadTestsFromTestCase(TestPng)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
