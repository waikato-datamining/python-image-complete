import unittest
import os


class ImageCompleteTest(unittest.TestCase):

    def data_dir(self):
        """
        Returns the data directory.

        :return: the data directory
        :rtype: str
        """
        root_dir = os.path.dirname(__file__)
        data_dir = root_dir + os.sep + "data"
        return data_dir

    def data_file(self, fname):
        """
        Returns the full path for the file (without path) and returns it.
        :param fname: the filename (without path)
        :type fname: str
        :return: the full path
        :rtype: str
        """
        return self.data_dir() + os.sep + fname
