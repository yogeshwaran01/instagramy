"""
    instagramy.InstagramUser
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module scrape data
    of given Instagram User.

    Usage Example
    -------------
    ::

        from instagramy.InstagramUser import InstagramUser

        >>> user = InstagramUser('github')
        >>> user.is_verified
        >>> user.number_of_followers
        >>> user.biography

"""

from .core.parser import ParseUser
from .core.requests import get
from .core.exceptions import UsernameNotFound, HTTPError


class InstagramUser:
    """
    Class InstagramUser scrapes instagram user information
    >>> instagram_user = InstagramUser("github")
    >>> instagram_user.is_verified
    True
    >>> instagram_user.biography
    'Built for developers.'
    """

    def __init__(self, username: str):

        self.url = f"https://www.instagram.com/{username}/"
        self.user_data = self.get_json()

    def get_json(self) -> dict:
        """
        Return a dict of user information
        """
        try:
            html = get(self.url)
        except HTTPError:
            raise UsernameNotFound(self.url.split("/")[-2])
            
        parser = ParseUser()
        parser.feed(html)
        return parser.Data

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
    def email(self) -> str:
        """ Email of the given user """
        return self.user_data["business_email"]

    @property
    def website(self) -> str:
        """ Website of the given user """
        return self.user_data["external_url"]

    @property
    def number_of_followers(self) -> int:
        """ No.of Followers of the given user """
        return self.user_data["edge_followed_by"]["count"]

    @property
    def number_of_followings(self) -> int:
        """ No.of Following of the given user """
        return self.user_data["edge_follow"]["count"]

    @property
    def number_of_posts(self) -> int:
        """ No.of Post of the given user """
        return self.user_data["edge_owner_to_timeline_media"]["count"]

    @property
    def profile_picture_url(self) -> str:
        """ Profile picture url of the Given User """
        return self.user_data["profile_pic_url_hd"]

    @property
    def is_verified(self) -> bool:
        """ Verification status of the user """
        return self.user_data["is_verified"]

    @property
    def is_private(self) -> bool:
        """ Account type is Private """
        return self.user_data["is_private"]

    @property
    def posts(self) -> list:
        """
        Top 12 posts data of the given user
        """

        posts_lists = []
        posts_details = self.user_data["edge_owner_to_timeline_media"]["edges"]
        for i in posts_details:
            data = {}
            try:
                data["likes"] = i["node"]["edge_liked_by"]["count"]
            except (KeyError, TypeError):
                data["likes"] = None
            try:
                data["comments"] = i["node"]["edge_media_to_comment"]["count"]
            except (KeyError, TypeError):
                data["comments"] = None
            try:
                data["caption"] = i["node"]["accessibility_caption"]
            except (KeyError, TypeError):
                data["caption"] = None
            try:
                data["is_video"] = i["node"]["is_video"]
            except (KeyError, TypeError):
                data["is_video"] = None
            try:
                data["timestamp"] = i["node"]["taken_at_timestamp"]
            except (KeyError, TypeError):
                data["timestamp"] = None
            try:
                data["location"] = i["node"]["location"]
            except (KeyError, TypeError):
                data["location"] = None
            try:
                data["shortcode"] = i["node"]["shortcode"]
            except (KeyError, TypeError):
                data["shortcode"] = None
            try:
                data[
                    "post_url"
                ] = f'https://www.instagram.com/p/{i["node"]["shortcode"]}/'
            except (KeyError, TypeError):
                data["post_url"] = None
            try:
                data["display_url"] = i["node"]["display_url"]
            except (KeyError, TypeError):
                data["display_url"] = None
            posts_lists.append(data)
        return posts_lists

    @property
    def posts_display_urls(self) -> list:
        """
        Top 12 posts picture url of the given user
        """

        return [i["display_url"] for i in self.posts]

    @property
    def other_info(self) -> dict:
        """
        Other information about user
        """
        return {
            "is_private": self.user_data["is_private"],
            "is_verified": self.user_data["is_verified"],
            "is_business_account": self.user_data["is_business_account"],
            "is_joined_recently": self.user_data["is_joined_recently"],
            "has_ar_effects": self.user_data["has_ar_effects"],
            "has_clips": self.user_data["has_clips"],
            "has_guides": self.user_data["has_guides"],
            "has_channel": self.user_data["has_channel"],
        }

    def __str__(self) -> str:
        return f"{self.fullname} ({self.username}) -> {self.biography}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.username}')"
