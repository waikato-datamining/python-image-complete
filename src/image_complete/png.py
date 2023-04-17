from io import BytesIO
from .base import load, DEFAULT_CHECK_SIZE


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


def is_png_complete(img, strict=True, check_size=DEFAULT_CHECK_SIZE):
    """
    Checks whether the PNG image is complete.

    https://en.wikipedia.org/wiki/Portable_Network_Graphics#Critical_chunks
    http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html#Chunk-layout
    http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html#C.IEND

    :param img: the absolute path to the BMP image or a bytes/BytesIO object
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
        if data_len > 8:
            if strict:
                data.seek(data_len - 8, 0)
                marker = data.read(8)
                return (marker[0] == 73) and (marker[1] == 69) and (marker[2] == 78) and (marker[3] == 68)
            else:
                if check_size > data_len:
                    check_size = data_len
                data.seek(data_len - check_size, 0)
                buffer = data.read(check_size)
                for i in range(len(buffer) - 8):
                    if (buffer[i] == 73) and (buffer[i+1] == 69) and (buffer[i+2] == 78) and (buffer[i+3] == 68):
                        return True
                return False
        else:
            return False
    except:
        return False
