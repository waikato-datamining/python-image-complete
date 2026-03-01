from __future__ import annotations

from io import BytesIO
from pathlib import Path

from image_complete.base import DEFAULT_CHECK_SIZE
from image_complete.bmp import is_bmp, is_bmp_complete
from image_complete.gif import is_gif, is_gif_complete
from image_complete.jpg import is_jpg, is_jpg_complete
from image_complete.png import is_png, is_png_complete
from image_complete.webp import is_webp, is_webp_complete

EXT_TYPE_MAP = {
    '.bmp': 'bmp',
    '.gif': 'gif',
    '.jpg': 'jpg',
    '.jpeg': 'jpg',
    '.png': 'png',
    '.webp': 'webp'
}

TYPE_IS_FUNC_MAP = {
    "bmp": is_bmp,
    "gif": is_gif,
    "jpg": is_jpg,
    "png": is_png,
    "webp": is_webp
}


def get_image_type(img, check_consistency=False) -> str:
    """
    Checks whether the image type is supported.

    :param img: the absolute path to the image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :param check_consistency: if True then the file type will be determined by both extension and file signature, and they must match. Only used when img is a string (file path).
    :type check_consistency: bool
    :return: the file type (bmp, gif, jpg, png, webp) or None if not supported
    :rtype: str
    """
    if isinstance(img, bytes):
        img = BytesIO(img)

    if isinstance(img, (str, Path)):
        name = img.lower()
        for ext, t in EXT_TYPE_MAP.items():
            if name.endswith(ext):
                if check_consistency:
                    func = TYPE_IS_FUNC_MAP.get(t)
                    if func and func(img):
                        return t
                    else:
                        return 'inconsistent'
                else:
                    return t
        return 'unknown'
    elif isinstance(img, BytesIO):
        for t, func in TYPE_IS_FUNC_MAP.items():
            if func(img):
                return t
        return 'unknown'
    else:
        raise TypeError(f"Unsupported data type: {type(img)}")


def is_image_complete(img,
                      strict=True,
                      check_size=DEFAULT_CHECK_SIZE,
                      check_consistency=False):
    """
    Checks whether the image is complete. Auto-detects the type based on extension.
    If the type is not supported, it will throw an exception.

    :param img: the absolute path to the image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :param strict: if True then no junk data after actual data is allowed
    :type strict: bool
    :param check_size: the number of bytes from the end of the file to look for EOF marker (only used by: gif, jpg, png)
    :type check_size: int
    :param check_consistency: if True then the file type will be determined by both extension and file signature, and they must match. Only used when img is a string (file path).
    :type check_consistency: bool
    :return: True if complete
    :rtype: bool
    """
    if isinstance(img, bytes):
        img = BytesIO(img)

    image_type = get_image_type(img, check_consistency=check_consistency)

    if image_type == 'unknown':
        raise ValueError("Failed to determine file type!")
    elif image_type == 'inconsistent':
        raise ValueError(
            "File type is inconsistent between extension and file signature!")
    elif image_type == "bmp":
        return is_bmp_complete(img, strict=strict)
    elif image_type == "gif":
        return is_gif_complete(img, strict=strict, check_size=check_size)
    elif image_type == "jpg":
        return is_jpg_complete(img, strict=strict, check_size=check_size)
    elif image_type == "png":
        return is_png_complete(img, strict=strict, check_size=check_size)
    elif image_type == "webp":
        return is_webp_complete(img, strict=strict)
    else:
        raise ValueError("Failed to determine file type!")
