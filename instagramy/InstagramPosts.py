import json

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {"UserAgent": UserAgent().random}


class InstagramPost:
    """
    Class InstagramPost scrape the post information
    by given post id (From url of the post)
    https://www.instagram.com/p/<post_id>/
    https://www.instagram.com/p/CGeYX2OA61s/

    >>> post = InstagramPost("CGeYX2OA61s")
    >>> post.author
    '@virat.kohli'
    >>> post.number_of_likes
    2203830
    >>> post.number_of_comments
    4629
    """

    def __init__(self, post_id: str):
        self.post_id = post_id
        self.url = f"https://www.instagram.com/p/{post_id}/"
        self.post_details = self.post_detail()

    def post_detail(self) -> dict:
        soup = BeautifulSoup(
            requests.get(self.url, headers=headers).text, "html.parser"
        )
        data = str(soup.find("script", {"type": "application/ld+json"}))
        info = json.loads(
            data[data.find('{"@context":') : data.find('name"')][:-2] + "}"
        )
        post_details = {
            "caption": info["caption"],
            "uploaddate": info["uploadDate"],
            "author": info["author"]["alternateName"],
            "profile_page_url": info["author"]["mainEntityofPage"]["@id"],
            "likes": info["interactionStatistic"]["userInteractionCount"],
            "comments": info["commentCount"],
            "description": info["description"],
        }
        return post_details

    @property
    def number_of_likes(self) -> int:
        return int(self.post_details["likes"])

    @property
    def number_of_comments(self) -> int:
        return int(self.post_details["comments"])

    @property
    def author(self) -> str:
        return self.post_details["author"]

    @property
    def caption(self) -> str:
        return self.post_details["caption"]

    @property
    def description(self) -> str:
        return self.post_details["description"]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.post_id}')"

    def __str__(self) -> str:
        return f"Post ({self.post_id}) posted by {self.author} with {self.number_of_likes} likes"
