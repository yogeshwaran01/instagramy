import json

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {"UserAgent": UserAgent().random}


def extract_user_profile(script) -> dict:
    """
    May raise json.decoder.JSONDecodeError
    """
    data = script.contents[0]
    info = json.loads(data[data.find('{"config"') : -1])
    return info["entry_data"]["ProfilePage"][0]["graphql"]["user"]


def extract_hashtag(script) -> dict:
    """
    May raise json.decoder.JSONDecodeError
    """
    data = script.contents[0]
    info = json.loads(data[data.find('{"config"') : -1])
    return info["entry_data"]["TagPage"][0]["graphql"]["hashtag"]


class InstagramUser:
    """
    Class InstagramUser scrapes instagram user information
    >>> instagram_user = InstagramUser("github")
    >>> instagram_user.is_verified
    True
    >>> instagram_user.biography
    'Built for developers.'
    """

    def __init__(self, username):
        self.url = f"https://www.instagram.com/{username}/"
        self.user_data = self.get_json()

    def get_json(self) -> dict:
        """
        Return a dict of user information
        """
        html = requests.get(self.url, headers=headers).text
        scripts = BeautifulSoup(html, "html.parser").find_all("script")
        try:
            return extract_user_profile(scripts[4])
        except (json.decoder.JSONDecodeError, KeyError):
            return extract_user_profile(scripts[3])

    @property
    def username(self) -> str:
        return self.user_data["username"]

    @property
    def fullname(self) -> str:
        return self.user_data["full_name"]

    @property
    def biography(self) -> str:
        return self.user_data["biography"]

    @property
    def email(self) -> str:
        return self.user_data["business_email"]

    @property
    def website(self) -> str:
        return self.user_data["external_url"]

    @property
    def number_of_followers(self) -> int:
        return self.user_data["edge_followed_by"]["count"]

    @property
    def number_of_followings(self) -> int:
        return self.user_data["edge_follow"]["count"]

    @property
    def number_of_posts(self) -> int:
        return self.user_data["edge_owner_to_timeline_media"]["count"]

    @property
    def profile_picture_url(self) -> str:
        return self.user_data["profile_pic_url_hd"]

    @property
    def is_verified(self) -> bool:
        return self.user_data["is_verified"]

    @property
    def is_private(self) -> bool:
        return self.user_data["is_private"]

    @property
    def posts(self) -> list:
        """
        Only returns recent 12 post details
        User account must be non private account
        """

        posts_lists = []
        posts_details = self.user_data["edge_owner_to_timeline_media"]["edges"]
        for i in posts_details:
            data = {}
            try:
                data["url"] = i["node"]["display_url"]
            except (KeyError, TypeError):
                data["url"] = None
            try:
                data["likes"] = i["node"]["edge_liked_by"]["count"]
            except (KeyError, TypeError):
                data["likes"] = None
            try:
                data["comment"] = i["node"]["edge_media_to_comment"]["count"]
            except (KeyError, TypeError):
                data["comment"] = None
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
            posts_lists.append(data)
        return posts_lists

    @property
    def posts_url(self) -> list:
        """
        Only return recents 12 posts url
        User account must be non private account
        """

        return [i["url"] for i in self.posts]

    @property
    def other_info(self) -> dict:
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


class InstagramHashTag:
    """
    Class InstagramHashTag scrapes instagram hashtag information
    >>> hashtag = InstagramHashTag("python")
    >>> hashtag.number_of_posts
    3119668
    >>> instagram_user.posts_url
    """

    def __init__(self, tag):
        self.url = f"https://www.instagram.com/explore/tags/{tag}/"
        self.tag_data = self.get_json()

    def get_json(self) -> dict:
        """
        Return a dict of user information
        """
        html = requests.get(self.url, headers=headers).text
        scripts = BeautifulSoup(html, "html.parser").find_all("script")
        return extract_hashtag(scripts[3])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.tagname}')"

    def __str__(self) -> str:
        return f"{self.tagname} has {self.number_of_posts} posts"

    @property
    def tagname(self) -> str:
        return self.tag_data["name"]

    @property
    def profile_pic_url(self) -> str:
        return self.tag_data["profile_pic_url"]

    @property
    def number_of_posts(self) -> int:
        return self.tag_data["edge_hashtag_to_media"]["count"]

    @property
    def top_posts(self) -> list:
        """
        Return Only top posts details upto 70
        """

        post_lists = []
        nodes = self.tag_data["edge_hashtag_to_media"]["edges"]
        for node in nodes:
            data = {}
            try:
                data["url"] = node["node"]["display_url"]
            except:
                data["url"] = None
            try:
                data["likes"] = node["node"]["edge_liked_by"]["count"]
            except:
                data["likes"] = None
            try:
                data["comments"] = node["node"]["edge_media_to_comment"]["count"]
            except:
                data["comments"] = None
            try:
                data["is_video"] = node["node"]["is_video"]
            except:
                data["is_video"] = None
            try:
                data["timestamp"] = node["node"]["taken_at_timestamp"]
            except:
                data["timestamp"] = None
            try:
                data["caption"] = node["node"]["accessibility_caption"]
            except:
                data["caption"] = None
            post_lists.append(data)
        return post_lists

    @property
    def posts_url(self) -> list:
        """
        Return Only top posts urls upto 70
        """
        return [i["url"] for i in self.top_posts]
