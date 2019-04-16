import os


def is_png_complete(img_path):
    """
    Checks whether the PNG image is complete.

    http://en.wikipedia.org/wiki/JPEG#Syntax_and_structure

    :param img_path: the absolute path to the PNG image
    :type img_path: str
    :return: True if complete
    :rtype: bool
    """

    try:
        flen = os.path.getsize(img_path)
        if flen > 8:
            with open(img_path, "rb") as f:
                f.seek(flen - 8, 0)
                marker = f.read(8)
                return (marker[0] == 73) and (marker[1] == 69) and (marker[2] == 78) and (marker[3] == 68)
        else:
            return False
    except:
        return False
