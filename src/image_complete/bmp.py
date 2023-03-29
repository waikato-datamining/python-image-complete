import struct

from io import BytesIO
from .base import load


def is_bmp(img):
    """
    Checks whether the image represents a bitmap.

    https://en.wikipedia.org/wiki/BMP_file_format#File_structure

    :param img: the absolute path to the BMP image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :return: True if a bitmap
    :rtype: bool
    """
    data, _ = load(img)
    try:
        data.seek(0)
        header = data.read(2)
        return header in [b"BM", b"BA", b"CI", b"CP", b"IC", b"PT"]
    except:
        return False


def is_bmp_complete(img):
    """
    Checks whether the BMP image is complete.

    https://en.wikipedia.org/wiki/BMP_file_format#File_structure

    :param img: the absolute path to the BMP image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :return: True if complete
    :rtype: bool
    """
    try:
        data, data_len = load(img)
        if data is None:
            return False
        if data_len > 6:
            data.seek(2, 0)
            data = data.read(4)
            blen = struct.unpack('I', data)
            return blen[0] == data_len
        else:
            return False
    except:
        return False
