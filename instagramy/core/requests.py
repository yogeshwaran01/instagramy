""" Wrapper for urllib.request """

from typing import Any
import random
from urllib.request import Request
from urllib.request import urlopen

from .user_agent import user_agents


def get(url: str) -> Any:
    """
    Function send the HTTP requests to given site
    and return the html content of the webpage
    """

    request = Request(
        url=url, headers={"User-Agent": f"user-agent: {random.choice(user_agents)}"}
    )

    with urlopen(request) as response:
        html = response.read()

    return html.decode("utf-8")
