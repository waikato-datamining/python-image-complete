import struct

from io import BytesIO
from .base import load


def is_webp(img):
    """
    Checks whether the image represents a WebP image.

    https://developers.google.com/speed/webp/docs/riff_container

    :param img: the absolute path to the WebP image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :return: True if a bitmap
    :rtype: bool
    """
    data, _ = load(img)
    try:
        data.seek(0, 0)
        data = data.read(4)
        return data.decode("utf-8") == "RIFF"
    except:
        return False


def is_webp_complete(img):
    """
    Checks whether the WebP image is complete.

    https://developers.google.com/speed/webp/docs/riff_container

    :param img: the absolute path to the BMP image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :return: True if complete
    :rtype: bool
    """

    try:
        data, data_len = load(img)
        if data is None:
            return False
        if data_len > 8:
            # RIFF header?
            data.seek(0, 0)
            d = data.read(4)
            if d.decode("utf-8") != "RIFF":
                return False
            # check data length against file length
            data.seek(4, 0)
            data = data.read(4)
            d_len = struct.unpack('I', data)
            return d_len[0] == data_len - 8  # RIFF/4 + DATALEN/4 = 8
        else:
            return False
    except:
        return False
