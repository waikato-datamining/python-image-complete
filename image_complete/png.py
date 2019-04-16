import os


def is_png_complete(img_path):
    """
    Checks whether the PNG image is complete.

    http://en.wikipedia.org/wiki/JPEG#Syntax_and_structure

    :param img_path: the absolute path to the JPG image
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
                return (marker[0] == -1) and (marker[1] == -39)
        else:
            return False
    except:
        return False
