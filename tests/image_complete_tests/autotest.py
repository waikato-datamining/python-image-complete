import unittest
from .basetest import ImageCompleteTest
from image_complete.auto import is_image_complete


class TestAuto(ImageCompleteTest):

    def test_complete_gif(self):
        self.assertTrue(is_image_complete(self.data_file("complete.gif")))

    def test_complete_jpg(self):
        self.assertTrue(is_image_complete(self.data_file("complete.jpg")))

    def test_complete_png(self):
        self.assertTrue(is_image_complete(self.data_file("complete.png")))

    def test_complete_bmp(self):
        self.assertTrue(is_image_complete(self.data_file("complete.bmp")))

    def test_complete_webp(self):
        self.assertTrue(is_image_complete(self.data_file("complete.webp")))

    def test_incomplete_gif(self):
        self.assertFalse(is_image_complete(self.data_file("incomplete.gif")))

    def test_incomplete_jpg(self):
        self.assertFalse(is_image_complete(self.data_file("incomplete.jpg")))

    def test_incomplete_png(self):
        self.assertFalse(is_image_complete(self.data_file("incomplete.png")))

    def test_incomplete_bmp(self):
        self.assertFalse(is_image_complete(self.data_file("incomplete.bmp")))

    def test_incomplete_webp(self):
        self.assertFalse(is_image_complete(self.data_file("incomplete.webp")))

    def test_empty_gif(self):
        self.assertFalse(is_image_complete(self.data_file("empty.gif")))

    def test_empty_jpg(self):
        self.assertFalse(is_image_complete(self.data_file("empty.jpg")))

    def test_empty_png(self):
        self.assertFalse(is_image_complete(self.data_file("empty.png")))

    def test_empty_bmp(self):
        self.assertFalse(is_image_complete(self.data_file("empty.bmp")))

    def test_empty_webp(self):
        self.assertFalse(is_image_complete(self.data_file("empty.webp")))

    def test_complete_gif_content(self):
        self.assertTrue(is_image_complete(self.data_content("complete.gif")))

    def test_complete_jpg_content(self):
        self.assertTrue(is_image_complete(self.data_content("complete.jpg")))

    def test_complete_png_content(self):
        self.assertTrue(is_image_complete(self.data_content("complete.png")))

    def test_complete_bmp_content(self):
        self.assertTrue(is_image_complete(self.data_content("complete.bmp")))

    def test_complete_webp_content(self):
        self.assertTrue(is_image_complete(self.data_content("complete.webp")))

    def test_incomplete_gif_content(self):
        self.assertFalse(is_image_complete(self.data_content("incomplete.gif")))

    def test_incomplete_jpg_content(self):
        self.assertFalse(is_image_complete(self.data_content("incomplete.jpg")))

    def test_incomplete_png_content(self):
        self.assertFalse(is_image_complete(self.data_content("incomplete.png")))

    def test_incomplete_bmp_content(self):
        self.assertFalse(is_image_complete(self.data_content("incomplete.bmp")))

    def test_incomplete_webp_content(self):
        self.assertFalse(is_image_complete(self.data_content("incomplete.webp")))

    def test_junk_bmp_strict(self):
        self.assertFalse(is_image_complete(self.data_file("junk.bmp"), strict=True))

    def test_junk_bmp_strict_bytes(self):
        self.assertFalse(is_image_complete(self.data_content("junk.bmp"), strict=True))

    def test_junk_bmp_lenient(self):
        self.assertTrue(is_image_complete(self.data_file("junk.bmp"), strict=False))

    def test_junk_bmp_lenient_bytes(self):
        self.assertTrue(is_image_complete(self.data_content("junk.bmp"), strict=False))

    def test_junk_webp_strict(self):
        self.assertFalse(is_image_complete(self.data_file("junk.webp"), strict=True))

    def test_junk_gif_strict(self):
        self.assertFalse(is_image_complete(self.data_file("junk.gif"), strict=True))

    def test_junk_gif_strict_bytes(self):
        self.assertFalse(is_image_complete(self.data_content("junk.gif"), strict=True))

    def test_junk_gif_lenient(self):
        self.assertTrue(is_image_complete(self.data_file("junk.gif"), strict=False, check_size=50))

    def test_junk_gif_lenient_bytes(self):
        self.assertTrue(is_image_complete(self.data_content("junk.gif"), strict=False, check_size=50))

    def test_junk_gif_lenient_short(self):
        self.assertFalse(is_image_complete(self.data_file("junk.gif"), strict=False, check_size=5))

    def test_junk_gif_lenient_short_bytes(self):
        self.assertFalse(is_image_complete(self.data_content("junk.gif"), strict=False, check_size=5))

    def test_junk_jpg_strict(self):
        self.assertFalse(is_image_complete(self.data_file("junk.jpg"), strict=True))

    def test_junk_jpg_strict_bytes(self):
        self.assertFalse(is_image_complete(self.data_content("junk.jpg"), strict=True))

    def test_junk_jpg_lenient(self):
        self.assertTrue(is_image_complete(self.data_file("junk.jpg"), strict=False, check_size=50))

    def test_junk_jpg_lenient_bytes(self):
        self.assertTrue(is_image_complete(self.data_content("junk.jpg"), strict=False, check_size=50))

    def test_junk_jpg_lenient_short(self):
        self.assertFalse(is_image_complete(self.data_file("junk.jpg"), strict=False, check_size=5))

    def test_junk_jpg_lenient_short_bytes(self):
        self.assertFalse(is_image_complete(self.data_content("junk.jpg"), strict=False, check_size=5))

    def test_junk_png_strict(self):
        self.assertFalse(is_image_complete(self.data_file("junk.png"), strict=True))

    def test_junk_png_strict_bytes(self):
        self.assertFalse(is_image_complete(self.data_content("junk.png"), strict=True))

    def test_junk_png_lenient(self):
        self.assertTrue(is_image_complete(self.data_file("junk.png"), strict=False, check_size=50))

    def test_junk_png_lenient_bytes(self):
        self.assertTrue(is_image_complete(self.data_content("junk.png"), strict=False, check_size=50))

    def test_junk_png_lenient_short(self):
        self.assertFalse(is_image_complete(self.data_file("junk.png"), strict=False, check_size=5))

    def test_junk_png_lenient_short_bytes(self):
        self.assertFalse(is_image_complete(self.data_content("junk.png"), strict=False, check_size=5))

    def test_junk_webp_strict_bytes(self):
        self.assertFalse(is_image_complete(self.data_content("junk.webp"), strict=True))

    def test_junk_webp_lenient(self):
        self.assertTrue(is_image_complete(self.data_file("junk.webp"), strict=False))

    def test_junk_webp_lenient_bytes(self):
        self.assertTrue(is_image_complete(self.data_content("junk.webp"), strict=False))

    def test_unknown_type(self):
        try:
            is_image_complete(self.data_file("file.blah"))
            self.fail("should have failed with exception")
        except:
            pass


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    return unittest.TestLoader().loadTestsFromTestCase(TestAuto)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
