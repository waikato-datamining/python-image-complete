import os
import struct


def is_webp_complete(img_path):
    """
    Checks whether the WebP image is complete.

    https://developers.google.com/speed/webp/docs/riff_container

    :param img_path: the absolute path to the WebP image
    :type img_path: str
    :return: True if complete
    :rtype: bool
    """

    try:
        file_len = os.path.getsize(img_path)
        if file_len > 8:
            with open(img_path, "rb") as f:
                # RIFF header?
                f.seek(0, 0)
                data = f.read(4)
                if data.decode("utf-8") != "RIFF":
                    return False
                # check data length against file length
                f.seek(4, 0)
                data = f.read(4)
                data_len = struct.unpack('I', data)
                return data_len[0] == file_len - 8  # RIFF/4 + DATALEN/4 = 8
        else:
            return False
    except:
        return False
