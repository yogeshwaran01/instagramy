"""
    instagramy.InstagramLocation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module scrape data
    of given Instagram Location.

    Usage Example
    -------------
    ::

        >>> from instagramy.InstagramLocation import InstagramLocation

        >>> location = InstagramLocation('977862530', 'mrc-nagar')
        >>> location.number_of_posts
        3119668
        >>> location.address

"""

from .core.parser import Parser
from .core.parser import Viewer
from .core.parser import LocationParser
from .core.exceptions import LocationNotFound
from .core.exceptions import RedirectionError
from .core.exceptions import HTTPError
from .core.cache import Cache
from .core.requests import get


class InstagramLocation(LocationParser):
    r"""
    Scrapes instagram location information
    `https://www.instagram.com/explore/locations/<location_id>/<slug>`
    `https://www.instagram.com/explore/locations/977862530/mrc-nagar`

    :param location_id: Location id of the location
    :param slug: slug name of the location
    :param sessionid (optional): Session id of Instagram which is in browser cookies
    :param from_cache (optional): Get data from the cache of instagramy not from instagram

    >>> location = InstagramLocation('977862530', 'mrc-nagar')
    >>> location.number_of_posts
    3119668
    >>> location.address
    """

    def __init__(self, location_id: str, slug: str, sessionid=None, from_cache=False):
        self.url = f"https://www.instagram.com/explore/locations/{location_id}/{slug}"
        self.sessionid = sessionid
        location = location_id + "_" + slug
        cache = Cache("location")
        if from_cache:
            if cache.is_exists(location):
                self.location_data = cache.read_cache(location)
            else:
                data = self.get_json()
                cache.make_cache(
                    location, data["entry_data"]["LocationsPage"][0]["graphql"]["location"]
                )
                self.location_data = data["entry_data"]["LocationsPage"][0]["graphql"]["location"]
        else:
            data = self.get_json()
            cache.make_cache(
                location, data["entry_data"]["LocationsPage"][0]["graphql"]["location"]
            )
            try:
                self.location_data = data["entry_data"]["LocationsPage"][0]["graphql"]["location"]
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
        """ Get Location information from Instagram """

        try:
            html = get(self.url, sessionid=self.sessionid)
        except HTTPError:
            raise LocationNotFound(self.url.split("/")[-2] + "_" + self.url.split("/")[-1])
        parser = Parser()
        parser.feed(html)
        return parser.Data

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"

    def __str__(self) -> str:
        return f"{self.name} has {self.number_of_posts} posts"
