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

from .core.parser import ParseHashTag
from .core.requests import get
from .core.exceptions import HTTPError, HashTagNotFound


class InstagramHashTag:
    """
    Class InstagramHashTag scrapes instagram hashtag information
    >>> hashtag = InstagramHashTag("python")
    >>> hashtag.number_of_posts
    3119668
    >>> instagram_user.posts_display_urls
    """

    def __init__(self, tag: str):
        self.url = f"https://www.instagram.com/explore/tags/{tag}/"
        self.tag_data = self.get_json()

    def get_json(self) -> dict:
        """
        Return a dict of Hashtag information
        """
        try:
            html = get(self.url)
        except HTTPError:
            raise HashTagNotFound(self.url.split("/")[-2])
        parser = ParseHashTag()
        parser.feed(html)
        return parser.Data

    @property
    def tagname(self) -> str:
        """ Tagname of the Hagtag """
        return self.tag_data["name"]

    @property
    def profile_pic_url(self) -> str:
        """ Profile picture url of the Hagtag """
        return self.tag_data["profile_pic_url"]

    @property
    def number_of_posts(self) -> int:
        """ No.of posts in given Hashtag """
        return self.tag_data["edge_hashtag_to_media"]["count"]

    @property
    def top_posts(self) -> list:
        """
        Top post data (<70) in the given Hashtag
        """

        post_lists = []
        nodes = self.tag_data["edge_hashtag_to_media"]["edges"]
        for node in nodes:
            data = {}
            try:
                data["likes"] = node["node"]["edge_liked_by"]["count"]
            except (KeyError, TypeError):
                data["likes"] = None
            try:
                data["comments"] = node["node"]["edge_media_to_comment"]["count"]
            except (KeyError, TypeError):
                data["comments"] = None
            try:
                data["is_video"] = node["node"]["is_video"]
            except (KeyError, TypeError):
                data["is_video"] = None
            try:
                data["timestamp"] = node["node"]["taken_at_timestamp"]
            except (KeyError, TypeError):
                data["timestamp"] = None
            try:
                data["caption"] = node["node"]["accessibility_caption"]
            except (KeyError, TypeError):
                data["caption"] = None
            try:
                data["shortcode"] = node["node"]["shortcode"]
            except (KeyError, TypeError):
                data["shortcode"] = None
            try:
                data[
                    "post_url"
                ] = f'https://www.instagram.com/p/{node["node"]["shortcode"]}'
            except (KeyError, TypeError):
                data["post_url"] = None
            try:
                data["display_url"] = node["node"]["display_url"]
            except (KeyError, TypeError):
                data["display_url"] = None
            post_lists.append(data)
        return post_lists

    @property
    def posts_display_urls(self) -> list:
        """
        Top post (<70) in the given Hashtag
        """
        return [i["display_url"] for i in self.top_posts]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.tagname}')"

    def __str__(self) -> str:
        return f"{'#' + self.tagname} has {self.number_of_posts} posts"
