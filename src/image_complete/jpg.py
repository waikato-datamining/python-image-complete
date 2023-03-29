from io import BytesIO
from .base import load


def is_jpg(img):
    """
    Checks whether the image represents a JPG.

    http://en.wikipedia.org/wiki/JPEG#Syntax_and_structure

    :param img: the absolute path to the JPG image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :return: True if a bitmap
    :rtype: bool
    """
    data, _ = load(img)
    try:
        data.seek(0)
        header = data.read(2)
        return (header[0] == 0xFF) and (header[1] == 0xD8)
    except:
        return False


def is_jpg_complete(img):
    """
    Checks whether the JPG image is complete.

    http://en.wikipedia.org/wiki/JPEG#Syntax_and_structure

    :param img: the absolute path to the JPG image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :return: True if complete
    :rtype: bool
    """
    try:
        data, data_len = load(img)
        if data is None:
            return False
        if data_len > 2:
            data.seek(data_len - 2, 0)
            marker = data.read(2)
            return (marker[0] == 0xFF) and (marker[1] == 0xD9)
        else:
            return False
    except:
        return False
