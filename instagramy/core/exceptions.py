""" Exception classes raised by Instagramy """

from urllib.error import HTTPError


class BaseException(HTTPError):
    """ Base Exception for instagramy """

    def __init__(self, name: str):
        self.name = name


class UsernameNotFound(BaseException):
    """ Raise if Username not found in Instagram """

    def __str__(self):
        return f"InstagramUser('{self.name}') not Found"


class HashTagNotFound(BaseException):
    """ Raise if Hashtag not found in Instagram """

    def __str__(self):
        return f"InstagramHashtag('{self.name}')"


class PostIdNotFound(BaseException):
    """ Raise if Post id not found in Instagram """

    def __str__(self):
        return f"InstargramPost('{self.name}')"


class LocationNotFound(BaseException):
    """ Raise if Location not found in Instagram """

    def __str__(self):
        return f"InstargramLocation('{self.name}')"


class RedirectionError(Exception):
    """ Raise if Instagram Redirects it to Login Page """

    def __str__(self):
        return "Instagram Redirects you to login page, \
Try After Sometime or Reboot your PC \
Provide the sessionid to Login"
