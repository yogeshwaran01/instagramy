# -*- coding: utf-8 -*-
"""
    Instagramy
    ~~~~~~~~~~

    A python package for Instagram. It scarpe the Instagram
    contents.

    :license: MIT License
"""

__package__ = "instagramy"
__description__ = "A python package for Instagram. It scarpe the Instagram contents."
__url__ = "https://github.com/yogeshwaran01/instagramy"
__version__ = "4.3"
__author__ = "YOGESHWARAN R <yogeshin247@gmail.com>"
__license__ = "MIT License"
__copyright__ = "Copyright 2021 Yogeshwaran R"

__all__ = ["InstagramUser", "InstagramHashTag", "InstagramPost", "InstagramLocation"]

from .InstagramUser import InstagramUser
from .InstagramPost import InstagramPost
from .InstagramHashTag import InstagramHashTag
from .InstagramLocation import InstagramLocation
