import os
import urllib.request

from instagramy.InstagramUser import InstagramUser
from instagramy.InstagramPost import InstagramPost
from instagramy.InstagramHashTag import InstagramHashTag


def download_profile_pic(username: str, sessionid=None, filepath=None) -> tuple:
    """ Download Instagram User Profile Picture """

    user = InstagramUser(username, sessionid)
    if filepath is None:
        filepath = f"{username}.jpg"
    pic_url = user.profile_picture_url
    return urllib.request.urlretrieve(pic_url, filename=filepath)


def download_post(id: str, sessionid=None, filepath=None) -> tuple:
    """ Download Instagram Post """

    post = InstagramPost(id, sessionid)
    if filepath is None:
        filepath = f"{id}.mp4"
    post_url = post.post_source
    return urllib.request.urlretrieve(post_url, filename=filepath)


def download_hashtags_posts(tag: str, sessionid: str, count=1):
    """
    Download posts of particualar Hashtag
    - It create the directory with name of give tagname
    - Download given count of posts with name of post id
    """

    if count > 65:
        raise Exception("Count must be less than 65")

    tag = InstagramHashTag(tag, sessionid)
    posts_ids = [post.shortcode for post in tag.top_posts][:count]
    os.mkdir(tag.tagname)
    for posts_id in posts_ids:
        post = InstagramPost(posts_id, sessionid)
        post_link = post.post_source
        if post.type_of_post == "GraphVideo":
            urllib.request.urlretrieve(
                post_link, filename=f"{tag.tagname}/{posts_id}.mp4"
            )
        else:
            urllib.request.urlretrieve(
                post_link, filename=f"{tag.tagname}/{posts_id}.jpg"
            )

    return True
