""" Wrapper for urllib.request """

from urllib.request import Request
from urllib.request import urlopen

from .user_agent import headers


def get(url: str) -> str:
    """
    Function send the HTTP requests to given site
    and return the html content of the webpage
    """

    request = Request(url, headers=headers)

    with urlopen(request) as reponse:
        html = reponse.read()

    return html.decode("utf-8")
