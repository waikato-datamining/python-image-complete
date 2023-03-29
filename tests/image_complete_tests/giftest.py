import unittest
from .basetest import ImageCompleteTest
from image_complete.gif import is_gif_complete, is_gif


class TestGif(ImageCompleteTest):

    def test_complete_gif(self):
        self.assertTrue(is_gif_complete(self.data_file("complete.gif")))

    def test_incomplete_gif(self):
        self.assertFalse(is_gif_complete(self.data_file("incomplete.gif")))

    def test_empty_gif(self):
        self.assertFalse(is_gif_complete(self.data_file("empty.gif")))

    def test_complete_gif_bytes(self):
        self.assertTrue(is_gif_complete(self.data_content("complete.gif")))

    def test_incomplete_gif_bytes(self):
        self.assertFalse(is_gif_complete(self.data_content("incomplete.gif")))

    def test_empty_gif_bytes(self):
        self.assertFalse(is_gif_complete(self.data_content("empty.gif")))

    def test_complete_is_gif_bytes(self):
        self.assertTrue(is_gif(self.data_content("complete.gif")))

    def test_incomplete_is_gif_bytes(self):
        self.assertTrue(is_gif(self.data_content("incomplete.gif")))

    def test_empty_is_gif_bytes(self):
        self.assertFalse(is_gif(self.data_content("empty.gif")))


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    return unittest.TestLoader().loadTestsFromTestCase(TestGif)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
