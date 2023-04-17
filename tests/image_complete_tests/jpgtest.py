import unittest
from .basetest import ImageCompleteTest
from image_complete.jpg import is_jpg_complete, is_jpg


class TestJpg(ImageCompleteTest):

    def test_complete_jpg(self):
        self.assertTrue(is_jpg_complete(self.data_file("complete.jpg")))

    def test_incomplete_jpg(self):
        self.assertFalse(is_jpg_complete(self.data_file("incomplete.jpg")))

    def test_empty_jpg(self):
        self.assertFalse(is_jpg_complete(self.data_file("empty.jpg")))

    def test_complete_jpg_bytes(self):
        self.assertTrue(is_jpg_complete(self.data_content("complete.jpg")))

    def test_incomplete_jpg_bytes(self):
        self.assertFalse(is_jpg_complete(self.data_content("incomplete.jpg")))

    def test_empty_jpg_bytes(self):
        self.assertFalse(is_jpg_complete(self.data_content("empty.jpg")))

    def test_complete_is_jpg_bytes(self):
        self.assertTrue(is_jpg(self.data_content("complete.jpg")))

    def test_incomplete_is_jpg_bytes(self):
        self.assertTrue(is_jpg(self.data_content("incomplete.jpg")))

    def test_empty_is_jpg_bytes(self):
        self.assertFalse(is_jpg(self.data_content("empty.jpg")))

    def test_junk_jpg_strict(self):
        self.assertFalse(is_jpg_complete(self.data_file("junk.jpg"), strict=True))

    def test_junk_jpg_strict_bytes(self):
        self.assertFalse(is_jpg_complete(self.data_content("junk.jpg"), strict=True))

    def test_junk_jpg_lenient(self):
        self.assertTrue(is_jpg_complete(self.data_file("junk.jpg"), strict=False, check_size=50))

    def test_junk_jpg_lenient_bytes(self):
        self.assertTrue(is_jpg_complete(self.data_content("junk.jpg"), strict=False, check_size=50))

    def test_junk_jpg_lenient_short(self):
        self.assertFalse(is_jpg_complete(self.data_file("junk.jpg"), strict=False, check_size=5))

    def test_junk_jpg_lenient_short_bytes(self):
        self.assertFalse(is_jpg_complete(self.data_content("junk.jpg"), strict=False, check_size=5))


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    return unittest.TestLoader().loadTestsFromTestCase(TestJpg)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
