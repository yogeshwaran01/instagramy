import argparse

from .InstagramUser import InstagramUser
from .InstagramPost import InstagramPost
from .InstagramHashTag import InstagramHashTag


def _pprint(data):
    for key, value in data.items():
        if value is None:
            value = ""
        print("{:<10} {:<10} ".format(key, value))


def _user(username):
    user = InstagramUser(username)
    return {
        "Username": user.username,
        "Name": user.fullname,
        "Biography": user.biography,
        "Followers": user.number_of_followers,
        "Following": user.number_of_followings,
        "Posts": user.number_of_posts,
    }


def _post(post_id):
    post = InstagramPost(post_id)
    return {
        "Post Id": post.post_id,
        "Author": post.author,
        "Likes": post.number_of_likes,
        "Comments": post.number_of_comments,
        "Date": post.upload_date,
        "Caption": post.caption,
    }


def _tag(tag):
    t = InstagramHashTag(tag)
    return {"Hashtag": "#" + t.tagname, "Posts": t.number_of_posts}


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Scrape Instagram Users Informations, Posts Details, and Hashtags details"
    )

    parser.add_argument("-u", "--user", required=False, help="Instagram Username", type=str)
    parser.add_argument("-p", "--post", required=False, help="Instagram Post ID", type=str)
    parser.add_argument(
        "-t", "--tag", required=False, help="Instagram Hashtag name", type=str
    )

    args = parser.parse_args()

    username = args.user
    tag_name = args.tag
    post = args.post

    if username:
        _pprint(_user(username))
    elif tag_name:
        _pprint(_tag(tag_name))
    elif post:
        _pprint(_post(post))
