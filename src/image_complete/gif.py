from io import BytesIO
from .base import load, DEFAULT_CHECK_SIZE


def is_gif(img):
    """
    Checks whether the image represents a GIF.

    https://en.wikipedia.org/wiki/GIF#File_format

    :param img: the absolute path to the GIF image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :return: True if a GIF
    :rtype: bool
    """
    data, _ = load(img)
    try:
        data.seek(0)
        header = data.read(6)
        return header == b"GIF89a"
    except:
        return False


def is_gif_complete(img, strict=True, check_size=DEFAULT_CHECK_SIZE):
    """
    Checks whether the GIF image is complete.

    https://en.wikipedia.org/wiki/GIF#File_format

    :param img: the absolute path to the GIF image or a bytes/BytesIO object
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
        if data_len > 1:
            if strict:
                data.seek(data_len - 1, 0)
                marker = data.read(1)
                return marker[0] == 59
            else:
                if check_size > data_len:
                    check_size = data_len
                data.seek(data_len - check_size, 0)
                buffer = data.read(check_size)
                for b in buffer:
                    if b == 59:
                        return True
                return False
        else:
            return False
    except:
        return False
