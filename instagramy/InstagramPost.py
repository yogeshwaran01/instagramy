"""
    instagramy.InstagramPost
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module scrape Instagram Post data
    for given Instagram Post id.

    Usage Example
    -------------
    ::

        >>> from instagramy.InstagramHashtag import InstagramPost

        >>> post = InstagramPost('CGeYX2OA61s')
        >>> post.author
        >>> post.number_of_likes
        >>> post.number_of_comments

"""

from .core.parser import Viewer
from .core.parser import Parser
from .core.parser import PostParser
from .core.exceptions import PostIdNotFound
from .core.exceptions import RedirectionError
from .core.exceptions import HTTPError
from .core.cache import Cache
from .core.requests import get


class InstagramPost(PostParser):
    r"""
    Scrape the post information
    `https://www.instagram.com/p/<post_id>/`
    `https://www.instagram.com/p/CGeYX2OA61s/`

    :param post_id: Id of the Instagram post  (From url of the post)
    :param sessionid (optional): Session id of Instagram which is in browser cookies
    :param from_cache (optional): Get data from the cache of instagramy not from instagram

    >>> post = InstagramPost("CGeYX2OA61s")
    >>> post.author
    '@virat.kohli'
    >>> post.number_of_likes
    2203830
    >>> post.number_of_comments
    4629
    """

    def __init__(self, post_id: str, sessionid=None, from_cache=False):
        self.post_id = post_id
        self.url = f"https://www.instagram.com/p/{post_id}/"
        self.sessionid = sessionid
        cache = Cache("post")
        if from_cache:
            if cache.is_exists(post_id):
                data = cache.read_cache(post_id)
            else:
                data = self.get_json()
                cache.make_cache(
                    post_id,
                    data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"],
                )
        else:
            data = self.get_json()
            cache.make_cache(
                post_id, data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]
            )
        try:
            self.post_data = data["entry_data"]["PostPage"][0]["graphql"][
                "shortcode_media"
            ]
        except KeyError:
            raise RedirectionError
        if sessionid:
            self.viewer = Viewer(data=data["config"]["viewer"])
        else:
            self.viewer = None

    def get_json(self) -> dict:
        """ Get post information from Instagram """

        try:
            html = get(self.url, sessionid=self.sessionid)
        except HTTPError:
            raise PostIdNotFound(self.post_id)
        parser = Parser()
        parser.feed(html)
        info = parser.Data
        return info

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.post_id}')"

    def __str__(self) -> str:
        return f"Post ({self.post_id}) posted by {self.author} with {self.number_of_likes} likes"
