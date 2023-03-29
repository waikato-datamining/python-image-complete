import os

from io import BytesIO


def load(img):
    """
    Loads the data and returns it as BytesIO object and the associated length.

    :param img: the image to load
    :type img: str or bytes or BytesIO
    :return: tuple of BytesIO wrapper and length
    :rtype: tuple
    """
    if isinstance(img, bytes):
        img = BytesIO(img)
    if isinstance(img, BytesIO):
        return img, img.getbuffer().nbytes
    if isinstance(img, str):
        flen = os.path.getsize(img)
        with open(img, "rb") as f:
            img = BytesIO(f.read())
        return img, flen
    else:
        print("Unhandled data type: %s" % str(type(img)))
        return None, None
