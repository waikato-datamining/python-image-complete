import os
import struct


def is_bmp_complete(img_path):
    """
    Checks whether the BMP image is complete.

    https://en.wikipedia.org/wiki/BMP_file_format#File_structure

    :param img_path: the absolute path to the BMP image
    :type img_path: str
    :return: True if complete
    :rtype: bool
    """

    try:
        flen = os.path.getsize(img_path)
        if flen > 6:
            with open(img_path, "rb") as f:
                f.seek(2, 0)
                data = f.read(4)
                blen = struct.unpack('I', data)
                return blen[0] == flen
        else:
            return False
    except:
        return False
