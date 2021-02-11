""" Html Parser for various Instagram """

import json
from html.parser import HTMLParser

from .exceptions import RedirectionError
from .requests import get


class Parser(HTMLParser):

    """
    Class Parse the Static Html of the Instagram
    website and return the required Data as
    Python Dict

    This Class Inherits html.parser.HtmlParser
    """

    Data = {}

    def handle_data(self, data):
        if data.startswith("window._sharedData"):
            try:
                self.Data = json.loads(data[data.find('{"config"'): -1])
            except (KeyError, json.JSONDecodeError):
                raise RedirectionError
        else:
            pass


class Viewer:
    """
    User of Instagram currently Authenticated
    Parse the Current User data in Page
    """

    def __init__(self, **kwags):
        data = kwags.get("data")
        if data:
            self.user_data = data
        else:
            sessionid = kwags.get("sessionid")
            html = get("https://instagram.com", sessionid=sessionid)
            parser = Parser()
            parser.feed(html)
            self.user_data = parser.Data

    @property
    def username(self) -> str:
        """ Username of the given user """
        return self.user_data["username"]

    @property
    def fullname(self) -> str:
        """ Fullname of the given user """
        return self.user_data["full_name"]

    @property
    def biography(self) -> str:
        """ Biography of the given user """
        return self.user_data["biography"]

    @property
    def website(self) -> str:
        """ Website of the given user """
        return self.user_data["external_url"]

    @property
    def profile_picture_url(self) -> str:
        """ Profile picture url of the Given User """
        return self.user_data["profile_pic_url_hd"]

    @property
    def is_private(self) -> bool:
        """ Account type is Private """
        return self.user_data["is_private"]

    @property
    def is_joined_recently(self) -> bool:
        """ is user joined recently """
        return self.user_data["is_joined_recently"]

    @property
    def is_professional_account(self) -> bool:
        """ is user joined recently """
        return self.user_data["is_professional_account"]

    def __str__(self) -> str:
        return f"{self.fullname} ({self.username}) -> {self.biography}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.username}')"
