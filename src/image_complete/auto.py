from image_complete.bmp import is_bmp_complete
from image_complete.gif import is_gif_complete
from image_complete.jpg import is_jpg_complete
from image_complete.png import is_png_complete


def is_image_complete(img_path):
    """
    Checks whether the image is complete. Auto-detects the type based on extension.
    If the type is not supported, it will throw an exception.

    :param img_path: the absolute path to the JPG image
    :type img_path: str
    :return: True if complete
    :rtype: bool
    """

    name = img_path.lower()
    if name.endswith(".gif"):
        return is_gif_complete(img_path)
    elif name.endswith(".jpg") or name.endswith(".jpeg"):
        return is_jpg_complete(img_path)
    elif name.endswith(".png"):
        return is_png_complete(img_path)
    elif name.endswith(".bmp"):
        return is_bmp_complete(img_path)
    else:
        raise Exception("Unsupported file type: " + img_path)
