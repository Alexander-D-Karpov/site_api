from typing import IO
import imghdr
from PIL import Image

allowed_image_types = ["jpeg", "png", "gif", "bmp"]


def validate_and_resize_user_icon(image: IO) -> str | IO:
    """validate and resize image"""
    if not imghdr.what(image) in allowed_image_types:
        return "Incorrect image type"

    return Image.thumbnail((258, 258))
