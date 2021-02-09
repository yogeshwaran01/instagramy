from instagramy.InstagramUser import InstagramUser
from instagramy.InstagramHashTag import InstagramHashTag


def analyze_users_popularity(usernames: list, sessionid: str) -> dict:
    """ Functions return the required data to Analze Instagram users """
    followers = []
    following = []
    posts = []
    for username in usernames:
        user = InstagramUser(username, sessionid)
        followers.append(user.number_of_followers)
        following.append(user.number_of_followings)
        posts.append(user.number_of_posts)
    data = {
        "Usernames": usernames,
        "Followers": followers,
        "Following": following,
        "Posts": posts,
    }
    return data


def analyze_user_recent_posts(username: str, sessionid: str) -> dict:
    """ Functions return the required data to Analze Instagram user recent post """

    user = InstagramUser(username, sessionid)
    posts = user.posts
    urls = []
    likes = []
    comments = []
    for post in posts:
        urls.append(post["post_url"])
        likes.append(post["likes"])
        comments.append(post["comments"])

    return {"Posts": urls, "Likes": likes, "Comments": comments}


def analyze_hashtags(hashtags: list, sessionid: str) -> dict:
    """ Functions return the required data to Analze Instagram Hashtags """

    posts = []
    for hashtag in hashtags:
        tag = InstagramHashTag(hashtag, sessionid)
        posts.append(tag.number_of_posts)

    return {"Hashtag": hashtags, "Posts": posts}
