import os


def is_jpg_complete(img_path):
    """
    Checks whether the JPG image is complete.

    https://en.wikipedia.org/wiki/Portable_Network_Graphics#Critical_chunks
    http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html#Chunk-layout
    http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html#C.IEND

    :param img_path: the absolute path to the PNG image
    :type img_path: str
    :return: True if complete
    :rtype: bool
    """

    try:
        flen = os.path.getsize(img_path)
        if flen > 2:
            with open(img_path, "rb") as f:
                f.seek(flen - 2, 0)
                marker = f.read(2)
                return (marker[0] == 0xFF) and (marker[1] == 0xD9)
        else:
            return False
    except:
        return False
