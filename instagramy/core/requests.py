""" Wrapper for urllib.request """

import random
from typing import Any
from urllib.request import Request, urlopen

from .user_agent import user_agents


def get(url: str, sessionid=None) -> Any:
    """
    Function send the HTTP requests to Instagram and
    Login into Instagram with session id
    and return the Html Content
    """

    request = Request(
        url=url, headers={"User-Agent": f"user-agent: {random.choice(user_agents)}"}
    )
    if sessionid:
        request.add_header("Cookie", f"sessionid={sessionid}")
    with urlopen(request) as response:
        html = response.read()

    return html.decode("utf-8")
