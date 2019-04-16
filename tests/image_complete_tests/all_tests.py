import unittest
import image_complete_tests.autotest
import image_complete_tests.giftest
import image_complete_tests.jpgtest
import image_complete_tests.pngtest


def suite():
    """
    Returns the test suite.
    :return: the test suite
    :rtype: unittest.TestSuite
    """
    result = unittest.TestSuite()
    result.addTests(image_complete_tests.autotest.suite())
    result.addTests(image_complete_tests.giftest.suite())
    result.addTests(image_complete_tests.jpgtest.suite())
    result.addTests(image_complete_tests.pngtest.suite())
    return result


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
