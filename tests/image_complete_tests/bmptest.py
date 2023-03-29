import unittest
from .basetest import ImageCompleteTest
from image_complete.bmp import is_bmp_complete, is_bmp


class TestPng(ImageCompleteTest):

    def test_complete_bmp(self):
        self.assertTrue(is_bmp_complete(self.data_file("complete.bmp")))

    def test_incomplete_bmp(self):
        self.assertFalse(is_bmp_complete(self.data_file("incomplete.bmp")))

    def test_empty_bmp(self):
        self.assertFalse(is_bmp_complete(self.data_file("empty.bmp")))

    def test_complete_bmp_bytes(self):
        self.assertTrue(is_bmp_complete(self.data_content("complete.bmp")))

    def test_incomplete_bmp_bytes(self):
        self.assertFalse(is_bmp_complete(self.data_content("incomplete.bmp")))

    def test_empty_bmp_bytes(self):
        self.assertFalse(is_bmp_complete(self.data_content("empty.bmp")))

    def test_complete_is_bmp_bytes(self):
        self.assertTrue(is_bmp(self.data_content("complete.bmp")))

    def test_incomplete_is_bmp_bytes(self):
        self.assertTrue(is_bmp(self.data_content("incomplete.bmp")))

    def test_empty_is_bmp_bytes(self):
        self.assertFalse(is_bmp(self.data_content("empty.bmp")))


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    return unittest.TestLoader().loadTestsFromTestCase(TestPng)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
