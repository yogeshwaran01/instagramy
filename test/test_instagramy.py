from instagramy import InstagramUser
from instagramy import InstagramPost
from instagramy import InstagramHashTag


def test_user():
    user = InstagramUser('github')
    assert user.username == "github"

def test_tag():
    tag = InstagramHashTag('github')
    assert tag.tagname == 'github'

def test_post():
    post = InstagramPost('CGeYX2OA61s')
    assert post.author == '@virat.kohli'
