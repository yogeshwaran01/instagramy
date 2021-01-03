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

from .core.parser import ParsePost
from .core.requests import get
from .core.exceptions import PostIdNotFound, HTTPError


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

    def __init__(self, post_id: str):
        self.post_id = post_id
        self.url = f"https://www.instagram.com/p/{post_id}/"
        self.post_details = self.post_detail()

    def post_detail(self) -> dict:
        """
        Return a dict of Post information
        """

        try:
            html = get(self.url)
        except HTTPError:
            raise PostIdNotFound(self.post_id)
        parser = ParsePost()
        parser.feed(html)
        info = parser.Data
        post_details = {}
        try:
            post_details["caption"] = info["caption"]
        except (KeyError, TypeError):
            post_details["caption"] = None
        try:
            post_details["uploaddate"] = info["uploadDate"]
        except (KeyError, TypeError):
            post_details["uploaddate"] = None
        try:
            post_details["author"] = info["author"]["alternateName"]
        except (KeyError, TypeError):
            post_details["author"] = None
        try:
            post_details["profile_page_url"] = info["author"]["mainEntityofPage"]["@id"]
        except (KeyError, TypeError):
            post_details["profile_page_url"] = None
        try:
            post_details["likes"] = info["interactionStatistic"]["userInteractionCount"]
        except (KeyError, TypeError):
            post_details["likes"] = None
        try:
            post_details["comments"] = info["commentCount"]
        except (KeyError, TypeError):
            post_details["comments"] = None
        try:
            post_details["description"] = info["description"]
        except (KeyError, TypeError):
            post_details["description"] = None

        return post_details

    @property
    def number_of_likes(self) -> int:
        """ No.of Like is given post """
        return int(self.post_details["likes"])

    @property
    def number_of_comments(self) -> int:
        """ No.of Comments is given post """
        return int(self.post_details["comments"])

    @property
    def author(self) -> str:
        """ Author of the Post """
        return self.post_details["author"]

    @property
    def caption(self) -> str:
        """ Caption of the Post """
        return self.post_details["caption"]

    @property
    def description(self) -> str:
        """ Discription of the Post given by Instagram """
        return self.post_details["description"]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.post_id}')"

    def __str__(self) -> str:
        return f"Post ({self.post_id}) posted by {self.author} with {self.number_of_likes} likes"
