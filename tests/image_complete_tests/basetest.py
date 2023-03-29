import unittest
import os

from io import BytesIO


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

    def data_content(self, fname):
        """
        Returns the content of the file (without path).
        :param fname: the filename (without path)
        :type fname: str
        :return: the content
        :rtype: bytes
        """
        with open(self.data_dir() + os.sep + fname, "rb") as fp:
            return BytesIO(fp.read())
