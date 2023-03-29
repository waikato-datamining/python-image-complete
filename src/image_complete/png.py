from io import BytesIO
from .base import load


def is_png(img):
    """
    Checks whether the image represents a PNG.

    https://en.wikipedia.org/wiki/Portable_Network_Graphics#Critical_chunks

    :param img: the absolute path to the PNG image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :return: True if a bitmap
    :rtype: bool
    """
    data, _ = load(img)
    try:
        data.seek(1)
        header = data.read(3)
        return header in [b"PNG"]
    except:
        return False


def is_png_complete(img):
    """
    Checks whether the PNG image is complete.

    https://en.wikipedia.org/wiki/Portable_Network_Graphics#Critical_chunks
    http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html#Chunk-layout
    http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html#C.IEND

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
            data.seek(data_len - 8, 0)
            marker = data.read(8)
            return (marker[0] == 73) and (marker[1] == 69) and (marker[2] == 78) and (marker[3] == 68)
        else:
            return False
    except:
        return False
