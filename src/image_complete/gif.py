from io import BytesIO
from .base import load


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


def is_gif_complete(img):
    """
    Checks whether the GIF image is complete.

    https://en.wikipedia.org/wiki/GIF#File_format

    :param img: the absolute path to the GIF image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :return: True if complete
    :rtype: bool
    """
    try:
        data, data_len = load(img)
        if data is None:
            return False
        if data_len > 1:
            data.seek(data_len - 1, 0)
            marker = data.read(1)
            return marker[0] == 59
        else:
            return False
    except:
        return False
