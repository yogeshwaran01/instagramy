""" Html Parsers for various Instagram pages """

import json
from html.parser import HTMLParser

from .exceptions import RedirectionError


class ParseUser(HTMLParser):

    """
    Class Parse the Static Html of the Instagram
    User website and return the required Data as
    Python Dict

    This Class Inherits html.parser.HtmlParser
    """

    Data = {}

    def handle_data(self, data):
        if data.startswith("window._sharedData"):
            try:
                self.Data = json.loads(data[data.find('{"config"'): -1])["entry_data"][
                    "ProfilePage"
                ][0]["graphql"]["user"]
            except (KeyError, json.JSONDecodeError):
                raise RedirectionError
        else:
            pass


class ParsePost(HTMLParser):

    """
    Class Parse the Static Html of the Instagram
    Post website and return the required Data as
    Python Dict

    This Class Inherits html.parser.HtmlParser
    """

    Data = {}

    def handle_data(self, data):
        if '{"@context"' in data:
            try:
                self.Data = json.loads(data.strip())
            except (KeyError, json.JSONDecodeError):
                raise RedirectionError
        else:
            pass


class ParseHashTag(HTMLParser):

    """
    Class Parse the Static Html of the Instagram
    HashTag website and return the required Data as
    Python Dict

    This Class Inherits html.parser.HtmlParser
    """

    Data = {}

    def handle_data(self, data):
        if data.startswith("window._sharedData"):
            try:
                self.Data = json.loads(data[data.find('{"config"'): -1])["entry_data"][
                    "TagPage"
                ][0]["graphql"]["hashtag"]
            except (KeyError, json.JSONDecodeError):
                raise RedirectionError
        else:
            pass
