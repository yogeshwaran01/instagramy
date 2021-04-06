"""
    instagramy.InstagramUser
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module scrape data
    of given Instagram User.

    Usage Example
    -------------
    ::

        >>> from instagramy.InstagramUser import InstagramUser

        >>> user = InstagramUser('github')
        >>> user.is_verified
        >>> user.number_of_followers
        >>> user.biography

"""

from .core.parser import Parser
from .core.parser import Viewer
from .core.parser import UserParser
from .core.exceptions import UsernameNotFound
from .core.exceptions import RedirectionError
from .core.exceptions import HTTPError
from .core.cache import Cache
from .core.requests import get


class InstagramUser(UserParser):
    r"""
    Scrapes instagram user information.

    :param username: Username of the Instagram user
    :param sessionid (optional): Session id of Instagram which is in browser cookies
    :param from_cache (optional): Get data from the cache of instagramy not from instagram

    >>> instagram_user = InstagramUser("github")
    >>> instagram_user.is_verified
    True
    >>> instagram_user.biography
    'Built for developers.'
    """

    def __init__(self, username: str, sessionid=None, from_cache=False):

        self.url = f"https://www.instagram.com/{username}/"
        self.sessionid = sessionid
        cache = Cache("user")
        if from_cache:
            if cache.is_exists(username):
                data = cache.read_cache(username)
            else:
                data = self.get_json()
                cache.make_cache(
                    username, data["entry_data"]["ProfilePage"][0]["graphql"]["user"]
                )
        else:
            data = self.get_json()
            cache.make_cache(
                username, data["entry_data"]["ProfilePage"][0]["graphql"]["user"]
            )
        try:
            self.user_data = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]
        except KeyError:
            raise RedirectionError
        if sessionid:
            self.viewer = Viewer(data=data["config"]["viewer"])
        else:
            self.viewer = None

    def get_json(self) -> dict:
        """ Get user information from Instagram """

        try:
            html = get(self.url, sessionid=self.sessionid)
        except HTTPError:
            raise UsernameNotFound(self.url.split("/")[-2])

        parser = Parser()
        parser.feed(html)
        return parser.Data

    def __str__(self) -> str:
        return f"{self.fullname} ({self.username}) -> {self.biography}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.username}')"
