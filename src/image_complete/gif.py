import os


def is_gif_complete(img_path):
    """
    Checks whether the GIF image is complete.

    https://en.wikipedia.org/wiki/GIF#File_format

    :param img_path: the absolute path to the GIF image
    :type img_path: str
    :return: True if complete
    :rtype: bool
    """

    try:
        flen = os.path.getsize(img_path)
        if flen > 1:
            with open(img_path, "rb") as f:
                f.seek(flen - 1, 0)
                marker = f.read(1)
                return marker[0] == 59
        else:
            return False
    except:
        return False
