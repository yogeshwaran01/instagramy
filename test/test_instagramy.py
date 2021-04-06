# Unable to fetch data from Instagram effectively
# So, Some data already store in other website to test the parsers
import unittest
import json

from instagramy.core.requests import get
from instagramy.plugins.manual_loading import *


# loading sample data for test from other website

user_data = json.loads(get("https://yogeshwaran01.herokuapp.com/user_data"))
post_data = json.loads(get("https://yogeshwaran01.herokuapp.com/post_data"))
tag_data = json.loads(get("https://yogeshwaran01.herokuapp.com/tag_data"))


class TestParsers(unittest.TestCase):
    def test_InstagramUser(self):
        user = InstagramUser(user_data)
        self.assertEqual(user.biography, "Built for developers.")
        self.assertIsNone(user.connected_fb_page)
        self.assertFalse(user.followed_by_viewer)
        self.assertFalse(user.follows_viewer)
        self.assertEqual(user.fullname, "GitHub")
        self.assertFalse(user.has_blocked_viewer)
        self.assertFalse(user.has_country_block)
        self.assertFalse(user.has_blocked_viewer)
        self.assertFalse(user.is_blocked_by_viewer)
        self.assertFalse(user.is_joined_recently)
        self.assertFalse(user.is_private)
        self.assertTrue(user.is_verified)
        self.assertAlmostEqual(user.no_of_mutual_follower, 0)
        self.assertAlmostEqual(user.number_of_followers, 139340)
        self.assertAlmostEqual(user.number_of_followings, 20)
        self.assertAlmostEqual(user.number_of_posts, 182)
        self.assertEqual(user.username, "github")

    def test_InstagramPost(self):
        post = InstagramPost(post_data)
        self.assertEqual(post.author, "chilll_memes")
        self.assertEqual(
            post.caption,
            "Photo by CHILL MEMES in MRC Nagar with @memepattarai2.0. May be a meme of 3 people and text that says 'private Hospital nurse Chilll_ memes Govt Hospital nurse'.",
        )
        self.assertEqual(post.number_of_comments, 0)
        self.assertEqual(post.number_of_likes, 21)

    def test_InstagramHashtag(self):
        tag = InstagramHashTag(tag_data)
        self.assertEqual(tag.number_of_posts, 3600401)
        self.assertEqual(tag.tagname, "python")
