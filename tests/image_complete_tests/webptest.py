import unittest
from .basetest import ImageCompleteTest
from image_complete.webp import is_webp_complete, is_webp


class TestPng(ImageCompleteTest):

    def test_complete_webp(self):
        self.assertTrue(is_webp_complete(self.data_file("complete.webp")))

    def test_incomplete_webp(self):
        self.assertFalse(is_webp_complete(self.data_file("incomplete.webp")))

    def test_empty_webp(self):
        self.assertFalse(is_webp_complete(self.data_file("empty.webp")))

    def test_complete_webp_bytes(self):
        self.assertTrue(is_webp_complete(self.data_content("complete.webp")))

    def test_incomplete_webp_bytes(self):
        self.assertFalse(is_webp_complete(self.data_content("incomplete.webp")))

    def test_empty_webp_bytes(self):
        self.assertFalse(is_webp_complete(self.data_content("empty.webp")))

    def test_complete_is_webp_bytes(self):
        self.assertTrue(is_webp(self.data_content("complete.webp")))

    def test_incomplete_is_webp_bytes(self):
        self.assertTrue(is_webp(self.data_content("incomplete.webp")))

    def test_empty_is_webp_bytes(self):
        self.assertFalse(is_webp(self.data_content("empty.webp")))


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    return unittest.TestLoader().loadTestsFromTestCase(TestPng)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
