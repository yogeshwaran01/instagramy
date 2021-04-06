"""
    instagramy.InstagramHashtag
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module scrape data
    of given Instagram Hashtag.

    Usage Example
    -------------
    ::

        from instagramy.InstagramHashtag import InstagramHashtag

        >>> tag = InstagramHashtag('python')
        >>> tag.number_of_posts
        >>> tag.top_posts

"""
from datetime import datetime
from collections import namedtuple

from .core.parser import Parser
from .core.parser import Viewer
from .core.parser import TagParser
from .core.exceptions import HashTagNotFound
from .core.exceptions import RedirectionError
from .core.exceptions import HTTPError
from .core.cache import Cache
from .core.requests import get


class InstagramHashTag(TagParser):
    """
    Class InstagramHashTag scrapes instagram hashtag information
    >>> hashtag = InstagramHashTag("python")
    >>> hashtag.number_of_posts
    3119668
    >>> instagram_user.posts_display_urls
    """

    def __init__(self, tag: str, sessionid=None, from_cache=False):
        self.url = f"https://www.instagram.com/explore/tags/{tag}/"
        self.sessionid = sessionid
        cache = Cache("tag")
        if from_cache:
            if cache.is_exists(tag):
                data = cache.read_cache(tag)
            else:
                data = self.get_json()
                cache.make_cache(
                    tag, data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]
                )
        else:
            data = self.get_json()
            cache.make_cache(
                tag, data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]
            )
        try:
            self.tag_data = data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]
        except KeyError:
            raise RedirectionError
        if sessionid:
            self.viewer = Viewer(data=data["config"]["viewer"])
        else:
            self.viewer = None

    def get_json(self) -> dict:
        """
        Return a dict of Hashtag information
        """
        try:
            html = get(self.url, sessionid=self.sessionid)
        except HTTPError:
            raise HashTagNotFound(self.url.split("/")[-2])
        parser = Parser()
        parser.feed(html)
        return parser.Data

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.tagname}')"

    def __str__(self) -> str:
        return f"{'#' + self.tagname} has {self.number_of_posts} posts"
