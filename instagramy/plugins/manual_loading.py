from instagramy.core.parser import UserParser
from instagramy.core.parser import TagParser
from instagramy.core.parser import PostParser


class InstagramUser(UserParser):
    def __init__(self, data: dict):
        self.user_data = data


class InstagramPost(PostParser):
    def __init__(self, data: dict):
        self.post_data = data


class InstagramHashTag(TagParser):
    def __init__(self, data: dict):
        self.tag_data = data
