"""
    instagramy.plugins.manual_loading
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Parse data of Instagram with manual feeding of Instagram Data in offline mode.
    This classes are more useful for data analysis purpose. Store the data in json
    file and Parse this data by using this classes instead of sending multiple requests
    to the Instagram

    Usage Example
    -------------
    ::
        >>> import json
        >>> from instagramy import InstagramUser

        >>> user = InstagramUser('github')
        >>> user_data = user.user_data

        # store data of user in json file
        >>> with open('github_user.json', 'w') as file_obj:
        ...     json.dump(user_data, file_obj)

        >>> from instagramy.plugins.manual_loading import InstagramUser

        # using the stored data
        >>> with open('github_user.json', 'r') as file_obj:
        ...     user_data = json.load(file_obj)
        >>> user = InstagramUser(user_data)
        >>> user.number_of_followers

"""

from instagramy.core.parser import UserParser
from instagramy.core.parser import TagParser
from instagramy.core.parser import PostParser


class InstagramUser(UserParser):
    r"""
    Parse the data of User from manual loading

    :param data: user_data from `instagramy.InstagramUser.user_data`
    """

    def __init__(self, data: dict):
        self.user_data = data


class InstagramPost(PostParser):
    r"""
    Parse the data of Post from manual loading

    :param data: user_data from `instagramy.InstagramPost.post_data`
    """

    def __init__(self, data: dict):
        self.post_data = data


class InstagramHashTag(TagParser):
    r"""
    Parse the data of hashtag from manual loading

    :param data: user_data from `instagramy.InstagramHashTag.tag_data`
    """

    def __init__(self, data: dict):
        self.tag_data = data
