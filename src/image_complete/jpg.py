from io import BytesIO
from .base import load, DEFAULT_CHECK_SIZE


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


def is_jpg_complete(img, strict=True, check_size=DEFAULT_CHECK_SIZE):
    """
    Checks whether the JPG image is complete.

    http://en.wikipedia.org/wiki/JPEG#Syntax_and_structure

    :param img: the absolute path to the JPG image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :param strict: if True then no junk data after actual data is allowed
    :type strict: bool
    :param check_size: the number of bytes from the end of the file to look for EOF marker
    :type check_size: int
    :return: True if complete
    :rtype: bool
    """
    try:
        data, data_len = load(img)
        if data is None:
            return False
        if data_len > 2:
            if strict:
                data.seek(data_len - 2, 0)
                marker = data.read(2)
                return (marker[0] == 0xFF) and (marker[1] == 0xD9)
            else:
                if check_size > data_len:
                    check_size = data_len
                data.seek(data_len - check_size, 0)
                buffer = data.read(check_size)
                for i in range(len(buffer) - 1):
                    if (buffer[i] == 0xFF) and (buffer[i+1] == 0xD9):
                        return True
                return False
        else:
            return False
    except:
        return False
