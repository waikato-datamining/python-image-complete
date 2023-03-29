import unittest
from .basetest import ImageCompleteTest
from image_complete.png import is_png_complete, is_png


class TestPng(ImageCompleteTest):

    def test_complete_png(self):
        self.assertTrue(is_png_complete(self.data_file("complete.png")))

    def test_incomplete_png(self):
        self.assertFalse(is_png_complete(self.data_file("incomplete.png")))

    def test_empty_png(self):
        self.assertFalse(is_png_complete(self.data_file("empty.png")))

    def test_complete_png_bytes(self):
        self.assertTrue(is_png_complete(self.data_content("complete.png")))

    def test_incomplete_png_bytes(self):
        self.assertFalse(is_png_complete(self.data_content("incomplete.png")))

    def test_empty_png_bytes(self):
        self.assertFalse(is_png_complete(self.data_content("empty.png")))

    def test_complete_is_png_bytes(self):
        self.assertTrue(is_png(self.data_content("complete.png")))

    def test_incomplete_is_png_bytes(self):
        self.assertTrue(is_png(self.data_content("incomplete.png")))

    def test_empty_is_png_bytes(self):
        self.assertFalse(is_png(self.data_content("empty.png")))


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    return unittest.TestLoader().loadTestsFromTestCase(TestPng)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
