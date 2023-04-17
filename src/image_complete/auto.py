from io import BytesIO

from image_complete.base import DEFAULT_CHECK_SIZE
from image_complete.bmp import is_bmp_complete, is_bmp
from image_complete.gif import is_gif_complete, is_gif
from image_complete.jpg import is_jpg_complete, is_jpg
from image_complete.png import is_png_complete, is_png
from image_complete.webp import is_webp_complete, is_webp


def is_image_complete(img, strict=True, check_size=DEFAULT_CHECK_SIZE):
    """
    Checks whether the image is complete. Auto-detects the type based on extension.
    If the type is not supported, it will throw an exception.

    :param img: the absolute path to the image or a bytes/BytesIO object
    :type img: str or bytes or BytesIO
    :param strict: if True then no junk data after actual data is allowed
    :type strict: bool
    :param check_size: the number of bytes from the end of the file to look for EOF marker (only used by: gif, jpg, png)
    :type check_size: int
    :return: True if complete
    :rtype: bool
    """
    if isinstance(img, bytes):
        img = BytesIO(img)

    if isinstance(img, str):
        name = img.lower()
        if name.endswith(".bmp"):
            return is_bmp_complete(img, strict=strict)
        elif name.endswith(".gif"):
            return is_gif_complete(img, strict=strict, check_size=check_size)
        elif name.endswith(".jpg") or name.endswith(".jpeg"):
            return is_jpg_complete(img, strict=strict, check_size=check_size)
        elif name.endswith(".png"):
            return is_png_complete(img, strict=strict, check_size=check_size)
        elif name.endswith(".webp"):
            return is_webp_complete(img, strict=strict)
        else:
            raise Exception("Unsupported file type: " + img)

    elif isinstance(img, BytesIO):
        if is_bmp(img):
            return is_bmp_complete(img, strict=strict)
        elif is_gif(img):
            return is_gif_complete(img, strict=strict, check_size=check_size)
        elif is_jpg(img):
            return is_jpg_complete(img, strict=strict, check_size=check_size)
        elif is_png(img):
            return is_png_complete(img, strict=strict, check_size=check_size)
        elif is_webp(img):
            return is_webp_complete(img, strict=strict)
        else:
            raise Exception("Failed to determine file type!")
    else:
        raise Exception("Unsupported data type: %s" % str(type(img)))