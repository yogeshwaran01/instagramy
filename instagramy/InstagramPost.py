"""
    instagramy.InstagramPost
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module scrape Instagram Post data
    for given Instagram Post id.

    Usage Example
    -------------
    ::

        from instagramy.InstagramHashtag import InstagramPost

        >>> post = InstagramPost('CGeYX2OA61s')
        >>> post.author
        >>> post.number_of_likes
        >>> post.number_of_comments

"""
from datetime import datetime

from .core.parser import Viewer
from .core.parser import Parser
from .core.exceptions import PostIdNotFound
from .core.exceptions import HTTPError
from .core.requests import get


class InstagramPost:
    """
    Class InstagramPost scrape the post information
    by given post id (From url of the post)
    `https://www.instagram.com/p/<post_id>/`
    `https://www.instagram.com/p/CGeYX2OA61s/`

    >>> post = InstagramPost("CGeYX2OA61s")
    >>> post.author
    '@virat.kohli'
    >>> post.number_of_likes
    2203830
    >>> post.number_of_comments
    4629
    """

    def __init__(self, post_id: str, sessionid=None):
        self.post_id = post_id
        self.url = f"https://www.instagram.com/p/{post_id}/"
        self.sessionid = sessionid
        data = self.get_json()
        self.post_details = data["entry_data"]["PostPage"][0]["graphql"][
            "shortcode_media"
        ]
        if sessionid:
            self.viewer = Viewer(data=data["config"]["viewer"])
        else:
            self.viewer = None

    def get_json(self) -> dict:
        """
        Return a dict of Post information
        """

        try:
            html = get(self.url, sessionid=self.sessionid)
        except HTTPError:
            raise PostIdNotFound(self.post_id)
        parser = Parser()
        parser.feed(html)
        info = parser.Data
        return info

    @property
    def type_of_post(self) -> str:
        """ Type of the Post"""
        return self.post_details["__typename"]

    @property
    def display_url(self) -> str:
        """ Display url of the Image/Video """
        return self.post_details["display_url"]

    @property
    def upload_time(self) -> datetime:
        """ Upload Datetime of the Post """
        return datetime.fromtimestamp(self.post_details["taken_at_timestamp"])

    @property
    def number_of_likes(self) -> int:
        """ No.of Like is given post """
        return int(self.post_details["edge_media_preview_like"]["count"])

    @property
    def number_of_comments(self) -> int:
        """ No.of Comments is given post """
        return int(self.post_details["edge_media_to_parent_comment"]["count"])

    @property
    def author(self) -> str:
        """ Author of the Post """
        return self.post_details["owner"]["username"]

    @property
    def caption(self) -> str:
        """ Caption of the Post """
        return self.post_details["accessibility_caption"]

    @property
    def post_source(self) -> str:
        """ Post Image/Video Link """
        if self.post_details["is_video"]:
            return self.post_details["video_url"]
        return self.display_url

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.post_id}')"

    def __str__(self) -> str:
        return f"Post ({self.post_id}) posted by {self.author} with {self.number_of_likes} likes"
