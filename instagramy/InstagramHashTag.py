"""
    instagramy.InstagramHashtag
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module scrape data
    of given Instagram Hashtag.

    Usage Example
    -------------
    ::

        >>> from instagramy.InstagramHashtag import InstagramHashtag

        >>> tag = InstagramHashtag('python')
        >>> tag.number_of_posts
        >>> tag.top_posts

"""

from .core.parser import Parser
from .core.parser import Viewer
from .core.parser import TagParser
from .core.exceptions import HashTagNotFound
from .core.exceptions import RedirectionError
from .core.exceptions import HTTPError
from .core.cache import Cache
from .core.requests import get


class InstagramHashTag(TagParser):
    r"""
    Scrapes instagram hashtag information

    :param tag: Name of the Instagram Hashtag
    :param sessionid (optional): Session id of Instagram which is in browser cookies
    :param from_cache (optional): Get data from the cache of instagramy not from instagram

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
                self.tag_data = cache.read_cache(tag)
            else:
                data = self.get_json()
                cache.make_cache(
                    tag, data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]
                )
                self.tag_data = data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]
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
            try:
                self.viewer = Viewer(data=data["config"]["viewer"])
            except UnboundLocalError:
                self.viewer = None
        else:
            self.viewer = None

    def get_json(self) -> dict:
        """ Get Hashtag information from Instagram """

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
